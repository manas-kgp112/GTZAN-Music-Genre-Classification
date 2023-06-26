# Importing standard libraries
import os
import sys
import cv2
import pandas as pd
import numpy as np
from dataclasses import dataclass
from sklearn.model_selection import train_test_split


# Logging and Exception
from src.logging import logger



# Config and sub-process scripts
from src.entity import DataTransformationConfig


'''
    This script executes the data transformation part of our project.
    It stores the transformed data in "artifacts/features" section of our project and provides necessary tools to prepare the
    data for futher model input preparation.

'''




class DataTransformation:
    def __init__(self, config:DataTransformationConfig):
        self.config = config


    def transform_spectrogram(self, spec, y_train, y_test):
        try:
            # SPLIT THE DATA INTO TRAINING DATA & TEST DATA
            spec_train ,spec_test= train_test_split(spec, test_size=0.2, random_state=42)

            # scaling features
            max_spec = np.amax(spec)
            spec_train = spec_train/max_spec
            spec_test = spec_test/max_spec

            spec_train = spec_train.astype(np.float32)
            spec_test = spec_test.astype(np.float32)

            # reshaping features
            N, row, col = spec_train.shape
            spec_train = spec_train.reshape((N, row, col, 1))

            N, row, col = spec_test.shape
            spec_test = spec_test.reshape((N, row, col, 1))

            # saving features
            np.savez_compressed(os.path.join(self.config.features_path, "spectrogram_features.npz"), spec_train=spec_train, spec_test=spec_test, y_train=y_train, y_test=y_test)
            logger.info(f"Spectrogram features exrtacted and saved at {os.path.join(self.config.features_path, 'spectrogram_features.npz')}")
        except Exception as e:
            raise e
        


    def transform_mfcc(self, mfcc, y_train, y_test):
        try:
            # SPLIT THE DATA INTO TRAINING DATA & TEST DATA
            mfcc_train ,mfcc_test= train_test_split(mfcc, test_size=0.2, random_state=42)

            # creating empty storages for reshaped features
            mfcc_train_new = np.empty((mfcc_train.shape[0], 120, 600))
            mfcc_test_new = np.empty((mfcc_test.shape[0], 120, 600))

            for i in range(mfcc_train.shape[0]):
                curr = mfcc_train[i]
                curr = cv2.resize(curr, (600, 120))
                mfcc_train_new[i] = curr

            mfcc_train = mfcc_train_new


            for i in range(mfcc_test.shape[0]):
                curr = mfcc_test[i]
                curr = cv2.resize(curr, (600, 120))
                mfcc_test_new[i] = curr

            mfcc_test = mfcc_test_new


            mfcc_train = mfcc_train.astype(np.float32)
            mfcc_test = mfcc_test.astype(np.float32)

            # reshaping features
            N, row, col = mfcc_train.shape
            mfcc_train = mfcc_train.reshape((N, row, col, 1))


            N, row, col = mfcc_test.shape
            mfcc_test = mfcc_test.reshape((N, row, col, 1))

            # scaling features
            mean_data = np.mean(mfcc_train)
            std_data = np.std(mfcc_train)


            mfcc_train = (mfcc_train - mean_data)/std_data
            mfcc_test = (mfcc_test - mean_data)/std_data


            # saving features
            np.savez_compressed(os.path.join(self.config.features_path, "mfcc_features.npz"), mfcc_train=mfcc_train, mfcc_test=mfcc_test, y_train=y_train, y_test=y_test)
            logger.info(f"MFCC features exrtacted and saved at {os.path.join(self.config.features_path, 'mfcc_features.npz')}")
        except Exception as e:
            raise e
        



    def transform_mel_spectrogram(self, mel_spec, y_train, y_test):
        try:
            # SPLIT THE DATA INTO TRAINING DATA & TEST DATA
            mel_spec_train ,mel_spec_test= train_test_split(mel_spec, test_size=0.2, random_state=42)

            # scaling features
            mel_spec_max = np.amax(mel_spec_train)
            mel_train = mel_spec_train/np.amax(mel_spec_max)
            mel_test = mel_spec_test/np.amax(mel_spec_max)

            mel_train = mel_train.astype(np.float32)
            mel_test = mel_test.astype(np.float32)

            # reshaping features
            N, row, col = mel_train.shape
            mel_train = mel_train.reshape((N, row, col, 1))

            N, row, col = mel_test.shape
            mel_test = mel_test.reshape((N, row, col, 1))

            # saving features
            np.savez_compressed(os.path.join(self.config.features_path, "mel_spectrogram_features.npz"), mel_train=mel_train, mel_test=mel_test, y_train=y_train, y_test=y_test)
            logger.info(f"Mel Spectrogram features exrtacted and saved at {os.path.join(self.config.features_path, 'mel_spectrogram_features.npz')}")
        except Exception as e:
            raise e





    def initiate_data_transformation(self):
        try:
            logger.info("initiating data transformation sequence")
            if os.path.exists(self.config.features_path):
                # loading data
                features = np.load(os.path.join(self.config.features_path, "MusicFeatures.npz"))
                '''transformation steps'''
                # extracting features
                spec = features['spec'] 
                mel_spec = features['mel'] 
                mfcc = features['mfcc'] 
                zcr = features['zcr'] 
                spec_c = features['cen'] 
                chr = features['chroma'] 
                y = features['target']

                # SPLIT THE TARGET INTO TRAIN AND TEST
                y_train, y_test  = train_test_split(y, test_size=0.2, random_state=42)
                
                
                # Data Transformation
                '''
                    1) spectrogram
                    2) mfcc
                    3) mel spectrogram
                '''
                self.transform_spectrogram(spec, y_train, y_test)
                self.transform_mfcc(mfcc, y_train, y_test)
                self.transform_mel_spectrogram(mel_spec, y_train, y_test)
            else:
                logger.error(f"Music Features file not found at {self.config.features_path}.")
                logger.error(f"Run the data_ingestion pipeline or check the directory permissions.")


        except Exception as e:
            raise e

