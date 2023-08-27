## common code which will be used in entire project..

import os
import sys
import pandas as pd
import numpy as np

from src.exception import CustomException
from src.logger import logging
import pickle
import dill

from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score


def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)
        # saving pathe to dir_path
        os.makedirs(dir_path, exist_ok=True)
        # making directory with dir_path
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
        logging.info(".pkl file saved successfully...!")

    except Exception as e:
        raise CustomException(e,sys)

def evaluate_models(X_train, y_train,X_test,y_test,models,param):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            para=param[list(models.keys())[i]]

            gs = GridSearchCV(model,para,cv=3)
            gs.fit(X_train,y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)

            #model.fit(X_train, y_train)  # Train model

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)

            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)
