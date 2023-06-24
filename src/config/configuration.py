# project pipeline scripts
from src.entity import (
    DataIngestionConfig,
    DataTransformationConfig,
    ModelTrainerConfig
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
            params = PARAMS_FILE_PATH,
            config = CONFIG_FILE_PATH):
        # storing variables
        self.config = read_yaml(config)
        self.params = read_yaml(params)


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

        # data_transformation_config creation
        data_transformation_config = DataTransformationConfig(
            file_path_30 = transformation_config.file_path_30,
            file_path_3 = transformation_config.file_path_3,
            transformed_data = transformation_config.transformed_data
        )

        logger.info("DataTransformationConfig extracted.")

        return data_transformation_config
    


    # ModelTrainerConfiguration Manager function
    def load_model_trainer_config(self) -> ModelTrainerConfig:

        trainer_config = self.config.model_trainer

        create_directories(trainer_config.save_model_path)

        # model_trainer_config creation
        model_trainer_config = ModelTrainerConfig(
            train_input_data = trainer_config.train_input_data,
            test_input_data = trainer_config.test_input_data,
            save_model_path = trainer_config.save_model_path
        )

        logger.info("ModelTrainerConfig extracted.")

        return model_trainer_config