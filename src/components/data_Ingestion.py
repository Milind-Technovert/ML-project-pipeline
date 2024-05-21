import os, sys
# Add the src directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import pandas as pd
import numpy as np
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
from src.exception import  CustomException
from src.logger import logging
from data_transformation import DataTransformation

@dataclass
class DataIngestionConfig:
    train_data_path=os.path.join("artifacts/data_ingestion","train.csv")
    test_data_path=os.path.join("artifacts/data_ingestion","test.csv")
    raw_data_path=os.path.join("artifacts/data_ingestion","raw.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data Ingestion started")
        try:
            logging.info("Data reading using pandas library from local system")
            data=pd.read_csv(os.path.join(r"C:\Users\milind.mali\DSP\ML-project-pipeline\Notebook\data","income_cleandata.csv"))
            logging.info("Data reading completed")

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info("Data splitted into train and test set")

            train_set,test_set=train_test_split(data, test_size=0.3, random_state=41)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Data Ingestion completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            logging.info("Error occured in data ingestion stage")
            raise CustomException(e,sys)
            raise e 
        

if __name__=="__main__":
    obj=DataIngestion()
    train_data_path, test_data_path =obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_arr, test_arr, _ =data_transformation.inititate_data_transformation(train_data_path,test_data_path)

