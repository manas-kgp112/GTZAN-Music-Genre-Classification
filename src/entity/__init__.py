# Importing standard libraries
from dataclasses import dataclass
from pathlib import Path



'''
    This script includes the configurations of the break up processes of our project such as :
    data_ingestion
    data_transformation
    etc ...

'''


@dataclass
class DataIngestionConfig:
    root_dir : Path
    file_path_30 : Path
    file_path_3 : Path