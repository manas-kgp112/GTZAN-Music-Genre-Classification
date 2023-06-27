# Importing standard libraries
import os
import sys
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras


# CNN architecture imports
from src.models.spec_cnn_architecture import CNN_spec
from src.models.mfcc_cnn_architecture import CNN_mfcc
from src.models.mel_spec_cnn_architecture import CNN_mel_spec


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

            logger.info("Input data extracted for model training..")


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
            logger.info("Loading all custom models.")
            # 1) spectrogram model
            cnn_spec = CNN_spec(input_shape=(spec_train[0].shape))
            spec_model = cnn_spec.compiled_model()

            # 2) mfcc model
            cnn_mfcc = CNN_mfcc(input_shape=(mfcc_train[0].shape))
            mfcc_model = cnn_mfcc.compiled_model()

            # 3) mel_spectrogram model
            cnn_mel_spec = CNN_mel_spec(input_shape=(mel_spec_train[0].shape))
            mel_spec_model = cnn_mel_spec.compiled_model()



            # <------ MODEL TRAINING ------->
            logger.info("Initialising checkpoints")

            # checkpoint initialization
            checkpoint_spec_model = keras.callbacks.ModelCheckpoint(os.path.join(self.config.save_model_path, "spec_model_{epoch:03d}.h5"), period=5)
            checkpoint_mfcc_model = keras.callbacks.ModelCheckpoint(os.path.join(self.config.save_model_path, "mfcc_model_{epoch:03d}.h5"), period=5)
            checkpoint_mel_spec_model = keras.callbacks.ModelCheckpoint(os.path.join(self.config.save_model_path, "mel_spec_model_{epoch:03d}.h5"), period=5)


            # fitting models
            logger.info("Training started for Spectrogram")
            spec_model.fit(
                spec_train,
                y_train,
                epochs=self.config.spec_epochs,
                callbacks=[checkpoint_spec_model],
                batch_size=self.config.spec_batch,
                verbose=self.config.spec_verbose
            )

            logger.info("Training started for MFCC")
            mfcc_model.fit(
                mfcc_train,
                y_train,
                epochs=self.config.mfcc_batch,
                callbacks=[checkpoint_mfcc_model],
                batch_size=self.config.mfcc_batch,
                verbose=self.config.mfcc_verbose
            )

            logger.info("Training started for MelSpectrogram")
            mel_spec_model.fit(
                mel_spec_train,
                y_train,
                epochs=self.config.mel_spec_batch,
                callbacks=[checkpoint_mel_spec_model],
                batch_size=self.config.mel_spec_batch,
                verbose=self.config.mel_spec_verbose
            )


            # saving models
            spec_model.save(os.path.join(self.config.save_model_path, "spectrogram.h5"))
            mfcc_model.save(os.path.join(self.config.save_model_path, "mfcc.h5"))
            mel_spec_model.save(os.path.join(self.config.save_model_path, "mel_spectrogram.h5"))

            logger.info(f"All models have been successfully saved at {self.config.save_model_path}")
        except Exception as e:
            raise e