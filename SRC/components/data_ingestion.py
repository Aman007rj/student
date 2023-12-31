import os
import sys
from SRC.exception import CustomException
from SRC.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from SRC.components.data_transformation import DataTransformation
from SRC.components.data_transformation import DataTransformationConfig
from SRC.components.model_trainer import ModelTrainer
from SRC.components.model_trainer import ModelTrainerConfig

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts', 'train.csv')
    test_data_path: str=os.path.join('artifacts', 'test.csv')
    raw_data_path: str=os.path.join('artifacts', 'raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info("inside data ingestion method")
        try:
            df = pd.read_csv('notebook\data\stud.csv')
            logging.info("dataset read")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("train test split started")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info('data ingestion completed')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e,sys)


if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    data_transfromation = DataTransformation()
    train_arr, test_arr = data_transfromation.initiate_data_transformation(train_data, test_data)

    modeltrainer = ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr, test_arr))


