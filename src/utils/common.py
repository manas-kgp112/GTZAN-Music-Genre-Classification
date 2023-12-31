# Importing standard libraries
import os
from ensure import ensure_annotations
from pathlib import Path
from box import ConfigBox
import yaml
import dill
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.metrics import confusion_matrix, accuracy_score, roc_auc_score, roc_curve, precision_score, recall_score, f1_score


# Custom logging
from src.logging import logger

# constants
from src.constants import class_names


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
    



def get_majority_vote(pred_arr:list):

    # This function takes the majority prediction as output out of all the predictions available for vote.

    try:
        len_pred = len(pred_arr[0])
        votes = []

        for i in len_pred:
            voters = [e[i] for e in pred_arr]
            voters = np.array(voters)

            # getting unique values
            uniq, freq = np.unique(voters, return_counts=True)
            max_val_index = np.argmax(freq)
            vote = uniq[max_val_index]

            votes.append(vote)


        votes = np.array(votes)
        return votes
    except Exception as e:
        raise e
    


def evaluate_performance(y_pred, y_true, config, feature):
    correct = len(y_pred) - np.count_nonzero(y_pred - y_true)
    acc = correct/ len(y_pred)
    acc = np.round(acc, 4) * 100

    print("Accuracy: ", correct, "/", len(y_pred), " = ", acc, "%")

    # class_names = ["Blues", "Classical", "Country", "Disco", "Hiphop", "Jazz", "Metal", "Pop", "Reggae", "Rock"]
    conf_mat = confusion_matrix(y_true, y_pred, normalize= 'true')
    conf_mat = np.round(conf_mat, 2)

    conf_mat_df = pd.DataFrame(conf_mat, columns= class_names, index= class_names)

    plt.figure(figsize = (10,7), dpi = 200)
    sns.set(font_scale=1.4)
    sns.heatmap(conf_mat_df, annot=True, annot_kws={"size": 16}) # font size
    plt.tight_layout()
    plt.savefig(os.path.join(config.plots_path, f"{feature}_conf_mat.png") + "/new_ensemble_mfcc_conf_mat.png")