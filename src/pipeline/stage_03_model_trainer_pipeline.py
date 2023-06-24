# Configuration Manager
from src.config.configuration import ConfigurationManager


# Custom logging
from src.logging import logger


# ModelTrainer module
from src.components.model_trainer import ModelTrainer


'''
    This script is the pipeline of model_trainer process.
    ModelTrainer will be executed here.

'''

class ModelTrainerPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        # loading the configuration manager
        configuration = ConfigurationManager()
        # extracting the model_trainer configuration from ConfigurationManager()
        model_trainer_config = configuration.load_model_trainer_config()

        # Initialising the ModelTrainer constructor
        model_trainer = ModelTrainer(config=model_trainer_config)
        # initiating model_trainer sequence
        model_trainer.initiate_model_trainer()
# ModelTrainerPipeline