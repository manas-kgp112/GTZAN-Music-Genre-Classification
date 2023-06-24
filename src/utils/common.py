# Importing standard libraries
import os
from ensure import ensure_annotations
from pathlib import Path
from box import ConfigBox
import yaml
import dill
from sklearn.metrics import confusion_matrix, accuracy_score, roc_auc_score, roc_curve, precision_score, recall_score, f1_score


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
    


def create_directories(file_path:Path) -> None:

    # This function creates directories with given path

    try:
        if os.path.exists(file_path):
            logger.info(f"Folder already exists at {file_path}")
        else:
            os.makedirs(file_path)

    except Exception as e:
        raise e
    


def save_object(object, file_path:str):

    # This function saves objects at particular file_path

    try:
        with open(file_path, "wb") as file_obj:
            dill.dump(object, file_obj)
    except Exception as e:
        raise e 
    



def train_model(model, model_title, X, Y, model_path):

    # This function evaluate a model's performace and stores the metrics in an array

    try:
        logger.info(f"Training initiated for {model_title}")
        model.fit(X, Y)
        save_object(model, os.path.join(model_path, f"{model_title}.pkl"))
    except Exception as e:
        raise e