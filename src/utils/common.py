# Importing standard libraries
from ensure import ensure_annotations
from pathlib import Path
from box import ConfigBox
import yaml


# Custom logging
from src.logging import logger


'''
    This script reads the .yaml (configuration/parameters) files
    and converts them into specific format for readability.

'''


@ensure_annotations
def read_yaml(file_path:Path) -> ConfigBox:
    
    # This function reads yaml files and converts them into ConfigBox datatype

    try:
        with open(file_path, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Loding yaml file: {file_path}... Status : successfull")
            return ConfigBox(content)
    except Exception as e:
        raise e