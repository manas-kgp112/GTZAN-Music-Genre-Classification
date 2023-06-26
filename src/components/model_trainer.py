# Importing standard libraries
import os
import sys
import pandas as pd
import numpy as np
from dataclasses import dataclass
from sklearn.metrics import confusion_matrix, accuracy_score, roc_auc_score, roc_curve


# CNN architecture imports
from src.models.spec_cnn_architecture import CNN_spec
from src.models.mfcc_cnn_architecture import CNN_mfcc
from src.models.mel_spec_cnn_architecture import CNN_mel_spec


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
        

    
    def get_input_data(self):
        try:
            spec_data = np.load(self.config.features_path, "spectrogram_features.npz")
            mfcc_data = np.load(self.config.features_path, "mfcc_features.npz")
            mel_spec_data = np.load(self.config.features_path, "mel_spectrogram_features.npz")

            spec_train = spec_data['spec_train']
            spec_test = spec_data['spec_test']
            mfcc_train = mfcc_data['mfcc_train']
            mfcc_test = mfcc_data['mfcc_test']
            mel_spec_train = mel_spec_data['mel_train']
            mel_spec_test = mel_spec_data['mel_test']
            y_train = spec_data['y_train']
            y_test = spec_data['y_test']


            return (
                spec_train,
                spec_test,
                mfcc_train,
                mfcc_test,
                mel_spec_train,
                mel_spec_test,
                y_train,
                y_test
            )
        except Exception as e:
            raise e


    def initiate_model_trainer(self):
        try:
            spec_train, spec_test, mfcc_train, mfcc_test, mel_spec_train, mel_spec_test, y_train, y_test = self.get_input_data()
            model_path = self.config.save_model_path

            # <---- Collecting compiled models ---->
            # 1) spectrogram model
            cnn_spec = CNN_spec(input_shape=(spec_train[0].shape))
            spec_model = cnn_spec.compiled_model()

            # 2) mfcc model
            cnn_mfcc = CNN_mfcc(input_shape=(mfcc_train[0].shape))
            mfcc_model = cnn_mfcc.compiled_model()

            # 3) mel_spectrogram model
            cnn_mel_spec = CNN_mel_spec(input_shape=(mel_spec_train[0].shape))
            mel_spec_model = cnn_mel_spec.compiled_model()
        except Exception as e:
            raise e