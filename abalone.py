# -*- coding: utf-8 -*-
""" Get test data about Abalone shells

Abalone shell data comes from the UCI Machine Learning Repository: https://archive.ics.uci.edu/ml/datasets/abalone

Detailed information can be found in the link.

Recommended target variable: rings [int]

References:
Dua, D. and Graff, C. (2019). UCI Machine Learning Repository. Available at: http://archive.ics.uci.edu/ml

Warwick J Nash, Tracy L Sellers, Simon R Talbot, Andrew J Cawthorn and Wes B Ford (1994). "The Population Biology of Abalone (_Haliotis_ species) in Tasmania. I. Blacklip Abalone (_H. rubra_) from the North Coast and Islands of Bass Strait", Sea Fisheries Division, Technical Report No. 48 (ISSN 1034-3288)

Created on Sun Sep 26 16:16:25 2021

@author: Joseph Huard
"""

import pandas as pd
import pathlib as plib

### META DATA
FILE_NAME = 'abalone' # Current File name goes here
DATA_ORIGIN_LINK = 'https://archive.ics.uci.edu/ml/datasets/abalone' # Where the data comes from goes here
TARGET_FEATURE = 'rings' # Recommended target feature goes here

HEADER_NAMES = [    # Specific header names for abalone data set
    'sex',
    'length',
    'diameter',
    'height',
    'whole_weight',
    'shucked_weight',
    'viscera_weight',
    'shell_weight',
    'rings'
]



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
    Retrieves data from either the corresponding csv in /data or from the web source.
    """
    current_dir = get_self_path()

    if check_data_presence(current_dir = current_dir):
        df = pd.read_csv(
            plib.Path(current_dir.parent).joinpath('data', f'{current_dir.stem}.csv')
        )
    else:
        df = pd.read_csv(
            r'https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data',
            names = HEADER_NAMES
        )

    return df


def default_data_cleanse(df: pd.DataFrame) -> pd.DataFrame:
    """
    Applies one-hot encoding to Sex of abolone.

    (Abalone data is already well curated.)
    """

    return pd.get_dummies(df, prefix = 'sex', columns = ['sex'])



if __name__ == "__main__":

    # Check for command line arguments
    import argparse as ap
    parser = ap.ArgumentParser(description = f"Loads data about {FILE_NAME} shells. Originally sourced from: {DATA_ORIGIN_LINK} \nRecommended target feature: {TARGET_FEATURE}.")
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