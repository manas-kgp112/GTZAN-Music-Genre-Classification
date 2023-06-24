# Configuration Manager
from src.config.configuration import ConfigurationManager


# Custom logging
from src.logging import logger


# ModelEvaluation module
from src.components.model_evaluation import ModelEvaluation


'''
    This script is the pipeline of model_evaluation process.
    ModelTrainer will be executed here.

'''

class ModelEvaluationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        # loading the configuration manager
        configuration = ConfigurationManager()
        # extracting the model_evaluation configuration from ConfigurationManager()
        model_evaluation_config = configuration.load_model_evaluation_config()

        # Initialising the ModelEvaluation constructor
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        # initiating model_evaluation sequence
        model_evaluation.initiate_model_evaluation()
# ModelEvaluationPipeline