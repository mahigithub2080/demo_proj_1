## common code which will be used in entire project..

import os
import sys
import pandas as pd
import numpy as np

from src.exception import CustomException
from src.logger import logging
import pickle
import dill

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
