# Importing standard libraries
import os
import sys
import pandas as pd
import numpy as np
from dataclasses import dataclass


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
from sklearn.metrics import confusion_matrix, accuracy_score, roc_auc_score, roc_curve


# Logging and Exception
from src.logging import logger



# Config and sub-process scripts
from src.entity import ModelTrainerConfig


'''
    This script executes the standard/custom model architecture.

'''



class ModelTrainer:
    def __init__(self, config:ModelTrainerConfig) -> None:
        self.config = config


    def initiate_model_trainer(self):
        try:
            pass
        except Exception as e:
            raise e