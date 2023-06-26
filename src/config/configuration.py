# project pipeline scripts
from src.entity import (
    DataIngestionConfig,
    DataTransformationConfig,
    ModelTrainerConfig,
    ModelEvalutionConfig
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

        # creating directory for data ingestion module storage
        create_directories(ingestion_config.features_path)

        # data_ingestion_config creation
        data_ingestion_config = DataIngestionConfig(
            root_dir = ingestion_config.root_dir,
            features_path = ingestion_config.features_path
        )
        
        logger.info("DataIngestionConfig extracted.")

        return data_ingestion_config
    


    # DataTransformationConfiguration Manager function
    def load_data_transformation_config(self) -> DataTransformationConfig:

        transformation_config = self.config.data_transformation

        # data_transformation_config creation
        data_transformation_config = DataTransformationConfig(
            features_path = transformation_config.features_path
        )

        logger.info("DataTransformationConfig extracted.")

        return data_transformation_config
    


    # ModelTrainerConfiguration Manager function
    def load_model_trainer_config(self) -> ModelTrainerConfig:

        trainer_config = self.config.model_trainer

        create_directories(trainer_config.save_model_path)

        # model_trainer_config creation
        model_trainer_config = ModelTrainerConfig(
            features_path = trainer_config.features_path,
            save_model_path = trainer_config.save_model_path
        )

        logger.info("ModelTrainerConfig extracted.")

        return model_trainer_config
    


    # ModelEvaluationConfiguration Manager function
    def load_model_evaluation_config(self) -> ModelEvalutionConfig:

        evaluation_config = self.config.model_evaluation

        create_directories(evaluation_config.metrics_path)
        create_directories(evaluation_config.plots_path)

        # model_evaluation_config creation
        model_evaluation_config = ModelEvalutionConfig(
            test_input_data = evaluation_config.test_input_data,
            model_path = evaluation_config.model_path,
            metrics_path = evaluation_config.metrics_path,
            plots_path = evaluation_config.plots_path
        )

        logger.info("ModelEvaluationConfig extracted.")

        return model_evaluation_config