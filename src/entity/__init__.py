# Importing standard libraries
from dataclasses import dataclass
from pathlib import Path



'''
    This script includes the datatypes (annotations) of the break up processes of our project such as :
    data_ingestion
    data_transformation
    etc ...

'''


@dataclass
class DataIngestionConfig:
    root_dir : Path
    file_path_30 : Path
    file_path_3 : Path


@dataclass
class DataTransformationConfig:
    file_path_30 : Path
    file_path_3 : Path
    transformed_data : Path


@dataclass
class ModelTrainerConfig:
    train_input_data : Path
    test_input_data : Path
    save_model_path : Path