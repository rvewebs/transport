from fastapi import FastAPI

from pydantic import BaseModel

# standard library imports
import pandas as pd
import numpy as np
import sklearn

#visualization
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

import xgboost as xgb
import optuna

from optuna.visualization.matplotlib import plot_param_importances

import mlflow


from sklearn.model_selection import cross_val_score

from sklearn.model_selection import train_test_split

from sklearn.pipeline import Pipeline as skl_pipeline

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, PowerTransformer

sklearn.set_config(transform_output='pandas')

# load metrics
from sklearn.metrics import mean_squared_error, mean_absolute_error

from typing import List
import typing

pd.set_option('display.float_format', '{:.3f}'.format)

# constant
RAND_ST = 345

model = joblib.load('model_test.joblib')


class DfRow(BaseModel):
    distance: int
    own_container: int
    complect_send: int
    container_train: int
    transportation_type: int
    days: int

class DataF(BaseModel):
    data: List[DfRow]


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Model prediction"}


@app.post("/predict")
async def predict(data:DataF):
    data_dict = data.dict()
    # print(data_dict['data'])
    print(pd.DataFrame(data_dict['data']))
    # print(pd.read_json({data_dict['data'], orient='records'))
        # predictions = model.predict(data)
    return  {'yes': 'yes'} # predictions # recive dataset, make prediction, return prediction,

@app.get("/test")
async def test():
    return {"Hello": "Api Fast"}

@app.get("/train/{item}")
async def train(item):
    return {"Train": item}
