# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 16:16:25 2021

@author: Joseph Huard
"""

import pandas as pd
import pathlib as plib

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
        return plib.Path('abalone.py').absolute()
    
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
    
    df = get_data()