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
from src.utils import save_object


@dataclass
class DatatransformationConfig:
    preprocessor_obj_filepath=os.path.join("artifacts","preprocessor.pkl") 
    # creating the path for preprocessor.pkl file...

class DataTransformation:
    def __init__(self) :
        self.data_transformation_config=DatatransformationConfig()
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
                    ("scalar",StandardScaler(with_mean=False)) # need to spcify with_mean=False for cat_pipeline
                ]
            )
            # creating pipeline for catagorical feature

            
            logging.info(f"num_pipeline created... and are numerical_fetures : {numerical_feature}")
            logging.info(f"cat_pipeline created... and are catagorical_feature : {catagorical_feature}")

            preprocessor=ColumnTransformer(
                [
                    ("num_pipeline",num_pipeline,numerical_feature),
                    ("cat_pipeline",cat_pipeline,catagorical_feature)
                ]
            ) 
            #combining num_pipeline and cat_pipeline in to one "preprocessor" object
            
            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)


    def initiate_data_transformation(self,train_path,test_path): #train_path,test_path will get from data_injestion file
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            logging.info("Read train and test data completed in data transformation file...!")

            target_column_name="math_score"
            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]

            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]
            # target column and independent columns are get seperated in test and train data..

            logging.info("Obtaining processor object start...!")
            preprocessor_obj=self.get_data_transformer_obj()

            logging.info("applying preprocessor_obj on training dataframe and testing dataframe...!")
            input_feature_train_arr=preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessor_obj.transform(input_feature_test_df)
            # it like  performing scalling on features of dataset.. 
            # but here all things are covered (missing_values/cat_to_num/transform_scaler) in preprocessor_obj..

            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]
            logging.info("preprocessor_obj applied ...Data convert to array format...!!!")

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_filepath, #path of processor.pkl file
                obj=preprocessor_obj #object of preprocessor mehotd..
            ) # calling save_object function of utils. to save the .pkl file on specified location..

            return(
                train_arr, #scaled train arr without target feature
                test_arr, #scaled test arr without target feature
                self.data_transformation_config.preprocessor_obj_filepath, # returning path of processor.pkl file
            )

        except Exception as e:
            raise CustomException(e,sys)




