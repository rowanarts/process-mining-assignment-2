"""


"""
from typing import Any

import pandas as pd
import pickle

PATH_EXCEL = '../dataset/bpi_challenge_2018_50mb.xlsx'  # original log, but saves as csv via Disco
PATH_DF_PARQUET = '../dataset/BPI_Challenge_df.parquet'  # same as .csv but much faster to load


# SAVING FILES
def _save_pickle(var: Any, path: str) -> None:
    with open(path, 'wb') as f:
        pickle.dump(var, f)


def save_parquet(frame: pd.DataFrame) -> None:
    frame.to_parquet(PATH_DF_PARQUET)


# LOADING FILES
def _load_pickle(path: str) -> Any:
    with open(path, 'rb') as f:
        var = pickle.load(f)
    return var

def load_excel() -> pd.DataFrame:
    return pd.read_excel(PATH_EXCEL)

def load_csv() -> pd.DataFrame:
    return pd.read_csv(PATH_CSV)


def load_parquet() -> pd.DataFrame:
    return pd.read_parquet(PATH_DF_PARQUET)
