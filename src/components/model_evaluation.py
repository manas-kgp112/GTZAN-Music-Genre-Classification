# Importing standard libraries
import os
import sys
import pandas as pd
import numpy as np
from dataclasses import dataclass
import pickle
from sklearn.metrics import confusion_matrix, accuracy_score, roc_auc_score, roc_curve, precision_score, recall_score, f1_score

# Logging and Exception
from src.logging import logger



# Config and sub-process scripts
from src.entity import ModelEvalutionConfig
from src.constants import models_dict


'''
    This script executes the model_evaluation part of our project.
    It collects the data from "artifacts" section of our project and provides necessary tools to evaluate
    performance of different models across various specific parameters.

'''




class ModelEvaluation:
    def __init__(self, config:ModelEvalutionConfig):
        self.config = config


    def get_test_data(self):
        try:
            test_data = pd.read_csv(self.config.test_input_data)

            Y_test = test_data["label"]
            X_test = test_data.drop(columns=["label"], axis=1)


            return (
                X_test,
                Y_test
            )
        
        except Exception as e:
            raise e


    def initiate_model_evaluation(self):
        try:
            logger.info("initiating model_evaluation sequence")

            # getting test data
            X_test, Y_test = self.get_test_data()

            if os.path.exists(self.config.model_path):
                        logger.info("Models avaiable for prediction pipeline injestion.")
                        models = models_dict

                        for model_name, model in models.items():
                            if os.path.exists(os.path.join(self.config.model_path, f"{model_name}.pkl")):

                                with open(os.path.join(self.config.model_path, f"{model_name}.pkl"), "rb") as obj:
                                     model = pickle.load(obj)

                                prediction = model.predict(X_test)
                                # performance analysis
                                accuracy = accuracy_score(Y_test, prediction)
                                precision = precision_score(Y_test, prediction, average='macro')
                                recall = recall_score(Y_test, prediction, average='macro')
                                f1 = f1_score(Y_test, prediction, average='macro')
                                # auc_roc = roc_auc_score(Y_test, prediction, multi_class='ovr')

                                # saving performance metrics
                                model_scores = {
                                    'Accuracy': accuracy,
                                    'Precision': precision,
                                    'Recall': recall,
                                    'F1 Score': f1,
                                    # 'AUC ROC' : auc_roc
                                }
                                performance_file = f"{model_name}.txt"

                                with open(os.path.join(self.config.metrics_path, performance_file), "w") as txt_file:
                                    for metric, score in model_scores.items():
                                        txt_file.write(f"{metric}: {score}\n")
                            else:
                                 logger.error(f"Model not found : {model_name}")
            else:
                logger.exception(f"Folder {self.config.model_path} do not exist.")
        except Exception as e:
            raise e

