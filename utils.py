import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
import numpy as np

DATA_PATH = 'dataset/BPI Challenge 2018.csv'


def load_data():
    return pd.read_csv(DATA_PATH)


def generate_outcome_two():
    data = generate_one_hot_encoding()
    data['Undesired Outcome 2'] = np.where((data['Change'] > 0) | data['Objection'] > 0, True, False)
    return data[['Case ID', 'Undesired Outcome 2']]



def generate_one_hot_encoding(data=None, level=1):
    if not data:
        data = load_data()[['Case ID', 'Activity']]

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

