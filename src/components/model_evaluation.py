# Importing standard libraries
import os
import sys
import pandas as pd
import numpy as np
from dataclasses import dataclass
import pickle
import tensorflow as tf
from tensorflow import keras
from sklearn.metrics import confusion_matrix, accuracy_score, roc_auc_score, roc_curve, precision_score, recall_score, f1_score

# Logging and Exception
from src.logging import logger



# Config, utils and sub-process scripts
from src.entity import ModelEvalutionConfig
from src.utils.common import (
    get_majority_vote,
    evaluate_performance
)


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
            spec_data = np.load(self.config.features_path, "spectrogram_features.npz")
            mfcc_data = np.load(self.config.features_path, "mfcc_features.npz")
            mel_spec_data = np.load(self.config.features_path, "mel_spectrogram_features.npz")

            # spec_train = spec_data['spec_train']
            spec_test = spec_data['spec_test']
            # mfcc_train = mfcc_data['mfcc_train']
            mfcc_test = mfcc_data['mfcc_test']
            # mel_spec_train = mel_spec_data['mel_train']
            mel_spec_test = mel_spec_data['mel_test']
            # y_train = spec_data['y_train']
            y_test = spec_data['y_test']

            logger.info("Test data extracted for model evluation..")


            return (
                # spec_train,
                spec_test,
                # mfcc_train,
                mfcc_test,
                # mel_spec_train,
                mel_spec_test,
                # y_train
                y_test
            )
        except Exception as e:
            raise e


    def initiate_model_evaluation(self):
        try:
            logger.info("initiating model_evaluation sequence")

            # getting test data
            spec_test, mfcc_test, mel_spec_test, y_test = self.get_test_data()

            if os.path.exists(self.config.save_model_path):
                logger.info("Models avaiable for prediction pipeline injestion.")

                # <----- MODEL EVLUATION ------>

                # loading models
                spec_model = keras.saving.load_model(os.path.join(self.config.save_model_path, "spectrogram.h5"))
                mfcc_model = keras.saving.load_model(os.path.join(self.config.save_model_path, "mfcc.h5"))
                mel_spec_model = keras.saving.load_model(os.path.join(self.config.save_model_path, "mel_spectrogram.h5"))


                # predictions
                y_pred_spec = spec_model.predict(spec_test)
                y_pred_mfcc = mfcc_model.predict(mfcc_test)
                y_pred_mel_spec = mel_spec_model.predict(mel_spec_test)

                # applying argmax {due to softmax layer}
                y_pred_spec = np.argmax(y_pred_spec, axis=-1)
                y_pred_mfcc = np.argmax(y_pred_mfcc, axis=-1)
                y_pred_mel_spec = np.argmax(y_pred_mel_spec, axis=-1)


                # majority vote {Ensembling}
                y_pred = get_majority_vote([y_pred_spec, y_pred_mfcc, y_pred_mel_spec])
                y_true = np.argmax(y_test, axis=-1)


                # evaluating performance
                evaluate_performance(y_pred=y_pred, y_true=y_true, config=self.config, feature="ensemble")
            else:
                logger.exception(f"Folder {self.config.model_path} do not exist.")
        except Exception as e:
            raise e

