# Importing standard libraries
import os
import sys
import pandas as pd
import numpy as np
from dataclasses import dataclass
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split


# Logging and Exception
from src.logging import logger



# Config and sub-process scripts
from src.entity import DataTransformationConfig


'''
    This script executes the data transformation part of our project.
    It stores the transformed data in "artifacts" section of our project and provides necessary tools to prepare the
    data for futher model input preparation.

'''




class DataTransformation:
    def __init__(self, config:DataTransformationConfig):
        self.config = config


    def initiate_data_transformation(self):
        try:
            logger.info("initiating data transformation sequence")
            if os.path.exists(self.config.file_path_30):
                features_30_df = pd.read_csv(self.config.file_path_30)
                logger.info(f"{self.config.file_path_30} sucessfully loaded.")
            if os.path.exists(self.config.file_path_30):
                features_3_df = pd.read_csv(self.config.file_path_3)
                logger.info(f"{self.config.file_path_3} sucessfully loaded.")


            # transformation steps
            features_3_df.drop(columns=["filename"], axis=1, inplace=True)
            col_list = features_3_df.columns.to_list()
            res_y = features_3_df.iloc[:, -1]
            res_x = features_3_df.iloc[:, :-1]
            label_encoder = LabelEncoder()
            standard_scaler = StandardScaler()
            Y = label_encoder.fit_transform(res_y)
            X = standard_scaler.fit_transform(np.array(res_x, dtype=float))

            # SPLIT THE DATA INTO TRAINING DATA & TEST DATA

            X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
            # dataset creation using train and test variables
            train_data = np.concatenate((X_train, Y_train.reshape(-1, 1)), axis=1)
            train_df = pd.DataFrame(train_data, columns=col_list)
            test_data = np.concatenate((X_test, Y_test.reshape(-1, 1)), axis=1)
            test_df = pd.DataFrame(test_data, columns=col_list)

            # saving csv's to given path
            train_df.to_csv(os.path.join(self.config.transformed_data, "train.csv"), index=False)
            test_df.to_csv(os.path.join(self.config.transformed_data, "test.csv"), index=False)


        except Exception as e:
            raise e

