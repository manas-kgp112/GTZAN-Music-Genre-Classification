# Importing standard libraries
import os
import sys
import pandas as pd
import numpy as np
from dataclasses import dataclass


# Logging and Exception
from src.logging import logger



# Config and sub-process scripts
from src.entity import DataIngestionConfig


'''
    This script executes the data ingestion part of our project.
    It collects the data from "artifacts" section of our project and provides necessary tools to prepare the
    data for futher applications/processing.

'''




class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config = config


    def initiate_data_ingestion(self):
        try:
            logger.info("initiating data_ingestion sequence")
            if os.path.exists(self.config.root_dir):
                if os.path.exists(self.config.file_path_30):
                    features_30_df = pd.read_csv(self.config.file_path_30)
                    logger.info(f"{self.config.file_path_30} sucessfully loaded.")
                if os.path.exists(self.config.file_path_30):
                    features_3_df = pd.read_csv(self.config.file_path_3)
                    logger.info(f"{self.config.file_path_3} sucessfully loaded.")
        except Exception as e:
            raise e

