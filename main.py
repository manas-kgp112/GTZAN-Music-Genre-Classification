# Importing pipelines
from src.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.pipeline.data_transformation_pipeline import DataTransformationPipeline




# Custom logging
from src.logging import logger


'''
    This script runs the complete project pipeline setup.

'''

STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
        raise e


STAGE_NAME = "Data Transformation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_transformation = DataTransformationPipeline()
   data_transformation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
        raise e