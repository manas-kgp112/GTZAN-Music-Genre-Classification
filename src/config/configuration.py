# project pipeline scripts
from src.entity import (
    DataIngestionConfig
)
from src.constants import *
from src.utils.common import read_yaml



# Configuration Manager

class ConfigurationManager:
    def __init__(
            self,
            config = CONFIG_FILE_PATH):
        # storing variables
        self.config = read_yaml(config)


    # DataIngestionConfiguration Manager function
    def load_data_ingestion_config(self) -> DataIngestionConfig:

        ingestion_config = self.config.data_ingestion

        # data_ingestion_config creation
        data_ingestion_config = DataIngestionConfig(
            root_dir = ingestion_config.root_dir,
            file_path_30 = ingestion_config.file_path_30,
            file_path_3 = ingestion_config.file_path_3
        )
        


        return data_ingestion_config