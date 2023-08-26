## purpose of data_transformation  is to do feature eng, data cleaning, convert cat to neumeric..etc
import numpy as np
import pandas as pd

import os
import sys
from dataclasses import dataclass

from sklearn.compose import ColumnTransformer # used to create pipeline
from sklearn.impute import SimpleImputer # handling missing data
from sklearn.pipeline import Pipeline # create pipeling
from sklearn.preprocessing import OneHotEncoder,StandardScaler # for transformation


from src.exception import CustomException
from src.logger import logging

@dataclass
class DatatransformationConfig:
    preprocessor_obj_filepath=os.path.join("artifacts","preprocessor.pkl") 
    # creating the path for preprocessor.pkl file...

class DataTransformation:
    def __init__(self) :
        self.datat_transformation_config=DatatransformationConfig()
        # creating obj of DatatransformationConfig class..

    def get_data_transformer_obj(self):
        """
         This method responsible to for data transformation...!!!...(missing_values/cat_to_num/transform_scaler)
        """
        try:
            numerical_feature=['reading_score','writing_score']
            catagorical_feature=[
                'gender',
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course"
            ]
            # numerical and catagorical features are seperated

            num_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="median")),
                    ("Scalar", StandardScaler())
                    ]
            ) 
            # creating pipeline for numerical feature
            cat_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="most_frequent")),
                    ("oneHotEncoder",OneHotEncoder()),
                    ("scalar",StandardScaler())
                ]
            )
            # creating pipeline for catagorical feature
            logging.info(f"num_pipeline created... and are numerical_fetures".format(numerical_feature))
            logging.info(f"cat_pipeline created... and are catagorical_feature".format(catagorical_feature))

            preprocessor=ColumnTransformer(
                [
                    ("num_pipeline",num_pipeline,numerical_feature)
                    ("cat_pipeline",cat_pipeline,catagorical_feature)
                ]
            ) 
            #combining num_pipeline and cat_pipeline in to one "preprocessor" object

            return preprocessor


        except Exception as e:
            raise CustomException(e,sys)




