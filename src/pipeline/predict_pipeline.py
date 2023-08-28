import pandas as pd
import numpy as np
import sys
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object # to load our .pkl file


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path='artifacts/model.pkl'
            processor_path='artifacts\preprocessor.pkl'
            model=load_object(file_path=model_path) # it will call the function from utils.py file
            preprocessor=load_object(file_path=processor_path)
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled) # this predict is built-in method of model...
            return preds
        
        except Exception as e:
            raise CustomException

 
class CustomData:
     # it will responsible in mapping all the input that we are giving in the HTML to the backend with these particular values
    def __init__(self,
        gender: str,
        race_ethnicity: str,
        parental_level_of_education,
        lunch: str,
        test_preparation_course: str,
        reading_score: int,
        writing_score: int):

        # saving data values in to class variable
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score


    def get_data_as_dataframe(self): # this function will convert the custom data in to dataframe formate and return dataframe..
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e,sys)