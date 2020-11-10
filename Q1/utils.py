"""


"""
from typing import Any

import pandas as pd
import pickle
import py4pm


PATH_CSV = '../dataset/BPI Challenge 2018.csv'  # original log, but saves as csv via Disco
PATH_DF_PARQUET = '../dataset/BPI Challenge_df.parquet'  # same as .csv but much faster to load
PATH_LOG = '../dataset/BPI Challenge 2018.xes'  # original log
PATH_LOG_PKL = '../dataset/BPI Challenge 2018'  # log object from pm4py module of the original log


# SAVING FILES
def _save_pickle(var: Any, path: str) -> None:
    with open(path, 'wb') as f:
        pickle.dump(var, f)


def save_parquet(frame: pd.DataFrame) -> None:
    frame.to_parquet(PATH_DF_PARQUET)


def save_log(log_object: py4pm) -> None:
    _save_pickle(log_object, PATH_LOG_PKL)


# LOADING FILES
def _load_pickle(path: str) -> Any:
    with open(path, 'rb') as f:
        var = pickle.load(f)
    return var


def load_csv() -> pd.DataFrame:
    return pd.read_csv(PATH_CSV)


def load_parquet() -> pd.DataFrame:
    return pd.read_parquet(PATH_DF_PARQUET)
