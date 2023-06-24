# Importing standard libraries
import os
import sys
import pandas as pd
import numpy as np
from dataclasses import dataclass
from sklearn.metrics import confusion_matrix, accuracy_score, roc_auc_score, roc_curve


# Standard Model imports
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from xgboost import XGBClassifier, XGBRFClassifier
from xgboost import plot_tree, plot_importance


# Logging and Exception
from src.logging import logger



# Config and sub-process scripts
from src.entity import ModelTrainerConfig


# Utility function
from src.utils.common import train_model


'''
    This script executes the standard/custom model architecture.

'''



class ModelTrainer:
    def __init__(self, config:ModelTrainerConfig) -> None:
        self.config = config


    def get_models(self) -> dict:
        try:
            models_dict = {
                "Naive Bayes" : GaussianNB(),
                "Stochastic Gradient Descent" : SGDClassifier(max_iter=5000, random_state=0),
                "KNN" : KNeighborsClassifier(n_neighbors=19),
                "Decision Tree" : DecisionTreeClassifier(),
                "Random Forest" : RandomForestClassifier(n_estimators=1000, max_depth=10, random_state=0),
                "Support Vector Machine" : SVC(),
                "Logistic Regression" : LogisticRegression(random_state=0, solver='lbfgs', multi_class='multinomial'),
                "Neural Nets" : MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5000, 10), random_state=1),
                "AdaBoost" : AdaBoostClassifier(n_estimators=1000),
                "XGBoost" : XGBClassifier(n_estimators=1000),
                "XGBRF Classifier" : XGBRFClassifier()
            }

            return models_dict
        except Exception as e:
            raise e
        

    
    def get_input_data(self) -> pd.DataFrame:
        try:
            train_data = pd.read_csv(self.config.train_input_data)

            Y_train = train_data["label"]
            X_train = train_data.drop(columns=["label"], axis=1)


            return (
                X_train,
                Y_train
            )
        except Exception as e:
            raise e


    def initiate_model_trainer(self):
        try:
            models = self.get_models()
            X_train, Y_train = self.get_input_data()

            model_path = self.config.save_model_path

            for model_name, model in models.items():
                train_model(model, model_name, X_train, Y_train, model_path)
                logger.info(f"Training succesfull for {model_name}")
                logger.info(f"Model exported {model_name}. Status : successfull")
        except Exception as e:
            raise e