# -*- coding: utf-8 -*-
"""Get test data about ...

... data comes from ___: 

Detailed information can be found in the link.

Recommended target variable: 

References:


Created on 

@author:
"""

import pandas as pd
import pathlib as plib

### META DATA
FILE_NAME = '' # Current File name goes here
DATA_ORIGIN_LINK = '' # Where the data comes from goes here
TARGET_FEATURE = '' # Recommended target feature goes here

### data access functions
def get_self_path() -> plib.WindowsPath:

    """
    Repturns directory path of this current file.
    """

    # checking if the function has been imported or called within the file
    if __name__ == "__main__":
        return plib.Path(f'{FILE_NAME}.py').absolute()
    
    return plib.Path(__file__).absolute()


def check_data_presence(current_dir: plib.Path) -> bool:
    """
    Will check to see if template data is already present within /data.
    
    returns: bool
    """
    return plib.Path(current_dir.parent).joinpath('data', f'{current_dir.stem}.csv').is_file()


def get_data() -> pd.DataFrame:
    """
    Retrieves data from either the corresponding csv in ./data/ or from the web source.
    """
    current_dir = get_self_path()

    if check_data_presence(current_dir = current_dir):
        df = pd.read_csv(
            plib.Path(current_dir.parent).joinpath('data', f'{current_dir.stem}.csv')
        )
    # else websource if applicable

    return df


def default_data_cleanse(df: pd.DataFrame) -> pd.DataFrame:
    pass


if __name__ == "__main__":

    # Check for command line arguments
    import argparse as ap
    parser = ap.ArgumentParser(description = f"Loads data about {FILE_NAME}. Originally sourced from: {DATA_ORIGIN_LINK} \nRecommended target feature: {TARGET_FEATURE}.")
    parser.add_argument(
        '--clean', 
        dest = 'cleanup', 
        action = 'store_const',
        const = True,
        default = False,
        help = "Data will have default cleaning process applied to it."
    )

    args = parser.parse_args(args = [])
    
    df = get_data() # load data

    # clean data if --clean argument was passed through command line.
    if args.cleanup:
        df = default_data_cleanse(df)
    
    print(df)