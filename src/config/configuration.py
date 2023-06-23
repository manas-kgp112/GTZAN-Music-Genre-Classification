# project pipeline scripts
from src.entity import (
    DataIngestionConfig,
    DataTransformationConfig
)
from src.constants import *
from src.utils.common import (
    read_yaml,
    create_directories
)


# Custom logging
from src.logging import logger


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
        
        logger.info("DataIngestionConfig extracted.")

        return data_ingestion_config
    


    # DataTransformationConfiguration Manager function
    def load_data_transformation_config(self) -> DataTransformationConfig:

        transformation_config = self.config.data_transformation

        # creating directory for transformed data
        create_directories(transformation_config.transformed_data)

        # data_ingestion_config creation
        data_transformation_config = DataTransformationConfig(
            file_path_30 = transformation_config.file_path_30,
            file_path_3 = transformation_config.file_path_3,
            transformed_data = transformation_config.transformed_data
        )


        return data_transformation_config