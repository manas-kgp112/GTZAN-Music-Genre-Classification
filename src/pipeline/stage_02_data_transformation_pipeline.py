# Configuration Manager
from src.config.configuration import ConfigurationManager


# Custom logging
from src.logging import logger


# DataTransformation module
from src.components.data_transformation import DataTransformation


'''
    This script is the pipeline of data_transformation process.
    data_transformation will be executed here.

'''

class DataTransformationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        # loading the configuration manager
        configuration = ConfigurationManager()
        # extracting the data_transformation configuration from ConfigurationManager()
        data_transformation_config = configuration.load_data_transformation_config()

        # Initialising the DataTransformation constructor
        data_transformation = DataTransformation(config=data_transformation_config)
        # initiating data_transformation sequence
        data_transformation.initiate_data_transformation()
# DataTransformation Pipeline