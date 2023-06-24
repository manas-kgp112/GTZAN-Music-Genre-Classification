# Configuration Manager
from src.config.configuration import ConfigurationManager


# Custom logging
from src.logging import logger


# DataIngestion module
from src.components.data_ingestion import DataIngestion


'''
    This script is the pipeline of data_ingestion process.
    DataIngestion will be executed here.

'''

class DataIngestionPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        # loading the configuration manager
        configuration = ConfigurationManager()
        # extracting the data_ingestion configuration from ConfigurationManager()
        data_ingestion_config = configuration.load_data_ingestion_config()

        # Initialising the DataIngestion constructor
        data_ingestion = DataIngestion(config=data_ingestion_config)
        # initiating data_ingestion sequence
        data_ingestion.initiate_data_ingestion()
# DataIngestionPipeline