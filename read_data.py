import pandas as pd

from datetime import datetime

__all__ = ["train_data", "test_data"]

f = pd.ExcelFile("./Mucuri_novo_semNaN_torre150m.xlsx")

df = f.parse("Dados anemo")

_train_data_1 = df[pd.to_datetime(df["Data"]) <= datetime(year=2015, month=12, day=22)]
_train_data_2 = df[
    (pd.to_datetime(df["Data"]) == datetime(year=2015, month=12, day=23))
    & (df["hora"] <= 11)
]

X_train = pd.concat([_train_data_1, _train_data_2]).drop("Data", axis=1)
Y_train = X_train.v_anemo2.shift(-1)

_test_data_1 = df[
    (pd.to_datetime(df["Data"]) == datetime(year=2015, month=12, day=23))
    & (df["hora"] >= 12)
]
_test_data_2 = df[
    (pd.to_datetime(df["Data"]) >= datetime(year=2015, month=12, day=24))
    & (pd.to_datetime(df["Data"]) <= datetime(year=2015, month=12, day=30))
]
_test_data_3 = df[
    (pd.to_datetime(df["Data"]) == datetime(year=2015, month=12, day=31))
    & (df["hora"] <= 13)
]

test_data = pd.concat([_test_data_1, _test_data_2, _test_data_3]).drop("Data", axis=1)
