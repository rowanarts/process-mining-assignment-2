import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
import numpy as np
import pickle
from typing import Any
import matplotlib.pyplot as plt

DATA_PATH = 'dataset/BPI Challenge 2018.csv'
PATH_EXCEL = 'dataset/bpi_challenge_2018_50mb.xlsx'  # original log, but saves as csv via Disco
PATH_DF_PARQUET = 'dataset/BPI_Challenge_df.parquet'  # same as .csv but much faster to load
PATH_UO1_DF_PARQUET = 'dataset/undesired_outcomes1_df.parquet'
PATH_LOG = 'dataset/BPI Challenge_log' 


"""


"""




# SAVING FILES
def _save_pickle(var: Any, path: str) -> None:
    with open(path, 'wb') as f:
        pickle.dump(var, f)


def save_parquet(frame: pd.DataFrame,undesired_outcomes=False ) -> None:
    if undesired_outcomes:
        frame.to_parquet(PATH_UO1_DF_PARQUET)
    
    else:
        frame.to_parquet(PATH_DF_PARQUET)


# LOADING FILES
def _load_pickle(path: str) -> Any:
    with open(path, 'rb') as f:
        var = pickle.load(f)
    return var

def load_excel() -> pd.DataFrame:
    return pd.read_excel(PATH_EXCEL)

def load_csv() -> pd.DataFrame:
    return pd.read_csv(DATA_PATH)


def load_parquet() -> pd.DataFrame:
    return pd.read_parquet(PATH_DF_PARQUET)

def load_log_original():
    return _load_pickle(PATH_LOG)

# --------------------------------------------------------------------------------------

# UTILS FUNCTION Q2 (MELVIN)


def generate_outcome_two():
    data = generate_one_hot_encoding()
    data['Undesired Outcome 2'] = np.where((data['Change'] > 0) | data['Objection'] > 0, True, False)
    return data[['Case ID', 'Undesired Outcome 2']]



def generate_one_hot_encoding(data=None, level=1):
    if not data:
        data = load_parquet()[['Case ID', 'Activity']]

    data['Sub Process'] = data['Activity'].apply(lambda x: x.split('-')[level])

    label_encoder = LabelEncoder()
    integer_encoded = label_encoder.fit_transform(data['Sub Process'])

    onehot_encoder = OneHotEncoder(sparse=False)
    integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
    onehot_encoded = onehot_encoder.fit_transform(integer_encoded)

    res = pd.DataFrame(onehot_encoded)
    res.columns = label_encoder.classes_
    res.index = data.index
    return data.merge(res, how='left', left_index=True, right_index=True)

