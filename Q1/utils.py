"""


"""
from typing import Any

import pandas as pd
import pickle
import py4pm

# input
PATH_LOG = '../dataset/BPI Challenge 2018.xes'  # original log FILE.
PATH_CSV = '../dataset/BPI Challenge 2018.csv'  # original log, but saveD as csv via Disco.

# transformed files, but still got all original data
PATH_DF_PARQUET = '../dataset/BPI Challenge_df.parquet'  # original log, but saved as .parquet file since it loads much faster.
PATH_LOG_PKL = '../dataset/BPI Challenge 2018'  # original log, loaded as csv/pickle, executed some data transformations and saved as pickle.

# filtered files
PATH_DF_PARQUET_FILTERED = '../dataset/BPI Challenge_df_filtered.parquet'  # filtered dataframe
PATH_LOG_PKL_FILTERED = '../dataset/BPI Challenge_log_filtered'  # filtered log object saved as pickle


# SAVING FILES
def _save_pickle(var: Any, path: str) -> None:
    with open(path, 'wb') as f:
        pickle.dump(var, f)


def save_parquet_original(frame: pd.DataFrame) -> None:
    frame.to_parquet(PATH_DF_PARQUET)


def save_log_original(log_object: py4pm) -> None:
    return _save_pickle(log_object, PATH_LOG_PKL)
    

def save_parquet_filtered(frame: pd.DataFrame) -> None:
    frame.to_parquet(PATH_DF_PARQUET_FILTERED)
    

def save_log_filtered(log_object: py4pm) -> None:
    return _save_pickle(log_object, PATH_LOG_PKL_FILTERED)


# LOADING FILES
def _load_pickle(path: str) -> Any:
    with open(path, 'rb') as f:
        var = pickle.load(f)
    return var


def load_csv() -> pd.DataFrame:
    return pd.read_csv(PATH_CSV)


def load_parquet_original() -> pd.DataFrame:
    return pd.read_parquet(PATH_DF_PARQUET)


def load_log_original():
    return _load_pickle(PATH_LOG_PKL)


def load_parquet_filtered() -> pd.DataFrame:
    return pd.read_parquet(PATH_DF_PARQUET_FILTERED)


def load_log_filtered():
    return _load_pickle(PATH_LOG_PKL_FILTERED)
