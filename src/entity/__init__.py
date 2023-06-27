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
    features_path: Path


@dataclass
class DataTransformationConfig:
    features_path: Path


@dataclass
class ModelTrainerConfig:
    features_path: Path
    save_model_path : Path
    spec_epochs: int
    spec_batch: int
    spec_verbose: int
    mfcc_epochs: int
    mfcc_batch: int
    mfcc_verbose: int
    mel_spec_epochs: int
    mel_spec_batch: int
    mel_spec_verbose: int



@dataclass
class ModelEvalutionConfig:
    test_input_data : Path
    model_path : Path
    metrics_path : Path
    plots_path : Path