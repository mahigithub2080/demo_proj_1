import os
import sys

import pandas as pd
from sklearn.model_selection import train_test_split

from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging 
from src.components.data_transformation import DatatransformationConfig
from src.components.data_transformation import DataTransformation

@dataclass
class DataInjestionConfig:
    train_data_path : str=os.path.join('artifacts','train.csv')
    test_data_path : str=os.path.join('artifacts','test.csv')
    raw_data_path : str=os.path.join('artifacts','data.csv')
    # created path for train/test/raw data

class DataInjestion:
    def __init__(self):
        self.injestion_config=DataInjestionConfig() 
        # assigning all the paths to the injestion_config object / Creating object of DataInjestionConfig

    def initiate_data_injestion(self):
        logging.info("Entered in to injestion method....!")
        try:
            df=pd.read_csv("notebook\data\stud.csv") # reading file 
            logging.info("read the dataset as DataFrame.....!")

            os.makedirs(os.path.dirname(self.injestion_config.train_data_path),exist_ok=True)  
            # creating the folders with the help of train data path
            # exist_ok --- if folder is already there.it will keep that folder

            df.to_csv(self.injestion_config.raw_data_path,index=False,header=True)
            # saving the raw data to specified path..

            logging.info("train_test_split initiated..!")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.injestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.injestion_config.test_data_path,index=False,header=True)
            # saving the train_set,test_set  data to specified path..

            logging.info("DataInjestion data completed....!")

            return(
                self.injestion_config.train_data_path,
                self.injestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj=DataInjestion()
    train_path,test_path=obj.initiate_data_injestion() 
    #calling method of DataInjestion Class which return the train/test data path

    data_transformation=DataTransformation()
    data_transformation.initiate_data_transformation(train_path,test_path) 
    #passing that path to transformation method of data_injestion file.. to perform transformation on train data and test data...
    # which return train and test data in array format
    
    





