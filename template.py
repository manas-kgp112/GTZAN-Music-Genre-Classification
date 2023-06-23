# Standard library import
import os
from pathlib import Path
import logging


# custom logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


'''
    This script defines the template to create the folder structure of the project.
    Run this script to obtain the folders mentioned in file_struct.
'''


# list of files and directories to be created.
file_struct = [
    f"main.py",
    f"src/__init__.py",
    f"config/config.yaml",
    f"src/components/__init__.py",
    f"src/utils/__init__.py",
    f"src/utils/common.py",
    f"src/logging/__init__.py",
    f"src/config/__init__.py",
    f"src/config/configuration.py",
    f"src/pipeline/__init__.py",
    f"src/entity/__init__.py",
    f"src/constants/__init__.py",
    f"res/GenreClassification.ipynb",
    f"res/DataIngestion.ipynb",
    f"res/DataTransformation.ipynb",
    f"res/ModelTrainer.ipynb",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    ".env",
    f"logs/init.txt",
    f"artifacts/models",
    f"artifacts/data",
]



# creating folders/dirs using the paths given
for file_path in file_struct:
    file_path = Path(file_path)
    file_dir, file_name = os.path.split(file_path)

    # creating folders
    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Created directory {file_dir}")

    # creating files
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, "w") as f:
            pass
            logging.info(f"Created empty file named : {file_path}")

    else:
        logging.info(f"File {file_path} already exists!")