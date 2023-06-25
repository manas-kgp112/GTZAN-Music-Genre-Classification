# Importing standard libraries
import os
import sys
import pandas as pd
import numpy as np
from dataclasses import dataclass
import librosa
from tqdm import tqdm
import tensorflow as tf

# Logging and Exception
from src.logging import logger



# Config and sub-process scripts
from src.entity import DataIngestionConfig
from src.utils.common import create_directories


'''
    This script executes the data ingestion part of our project.
    It collects the data from "artifacts" section of our project and provides necessary tools to prepare the
    data for futher applications/processing.

'''




class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config = config


    def extract_features(self, audio_paths, audio_labels):
        # creating storage spaces for features
        spec = np.empty([1000, 1025, 1293])
        mel_spec = np.empty([1000, 128, 1293])
        mfcc = np.empty([1000, 10, 1293])
        zcr = np.empty([1000, 1293])
        spec_c = np.empty([1000, 1293])
        chr = np.empty([1000, 12, 1293])
        bad_index = []
        for i in tqdm(range(len(audio_labels))):
            try:
                
                audio = audio_paths[i]
                y, r = librosa.load(audio)


                stft = librosa.stft(y)
                stft_db = librosa.amplitude_to_db(abs(stft))
                spec[i] = stft_db


                mel = librosa.feature.melspectrogram(y=y)
                mel_db = librosa.power_to_db(mel)
                mel_spec[i] = mel_db


                mfc = librosa.feature.mfcc(y=y, sr=r, n_mfcc=10)
                mfcc[i] = mfc


                zero = librosa.feature.zero_crossing_rate(y)[0]
                zcr[i] = zero


                spec_cent = librosa.feature.spectral_centroid(y=y, sr=r)[0]
                spec_c[i] = spec_cent


                chroma = librosa.feature.chroma_stft(y=y, sr=r, n_chroma=12, n_fft=4096)
                chr[i] = chroma

                return (
                    spec,
                    mel_spec,
                    mfcc,
                    zcr,
                    spec_c,
                    chr,
                    bad_index
                )


            except:
                bad_index.append(i)


    def initiate_data_ingestion(self):
        try:
            logger.info("initiating data_ingestion sequence")
            audio_labels = []
            audio_paths = []

            for root, dirs, files in os.walk(self.config.root_dir, topdown=False):
                for file in files:
                    if file.endswith(".wav"):
                        audio_paths.append(os.path.join(root, file))
                        label, _ = file.split(".", 1)
                        audio_labels.append(label)

            audio_labels = np.array(audio_labels)
            audio_paths = np.array(audio_paths)

            # Storing extracted features from audio samples
            spec, mel_spec, mfcc, zcr, spec_c, chr, bad_index = self.extract_features(audio_paths, audio_labels)


            # cleaning mal functioning data points
            spec = np.delete(spec, bad_index, 0)
            mel_spec = np.delete(mel_spec, bad_index, 0)
            mfcc = np.delete(mfcc, bad_index, 0)
            zcr = np.delete(zcr, bad_index, 0)
            spec_c = np.delete(spec_c, bad_index, 0)
            chr = np.delete(chr, bad_index, 0)
            audio_labels = np.delete(audio_labels, bad_index)

            # changing data types
            spec = spec.astype(np.float32)
            mel_spec = mel_spec.astype(np.float32)
            mfcc = mfcc.astype(np.float32)
            zcr = zcr.astype(np.float32)
            spec_c = spec_c.astype(np.float32)
            chr = chr.astype(np.float32)


            # converting target variables
            audio_labels[audio_labels == 'blues'] = 0
            audio_labels[audio_labels == 'classical'] = 1
            audio_labels[audio_labels == 'country'] = 2
            audio_labels[audio_labels == 'disco'] = 3
            audio_labels[audio_labels == 'hiphop'] = 4
            audio_labels[audio_labels == 'jazz'] = 5
            audio_labels[audio_labels == 'metal'] = 6
            audio_labels[audio_labels == 'pop'] = 7
            audio_labels[audio_labels == 'reggae'] = 8
            audio_labels[audio_labels == 'rock'] = 9
            audio_labels = [int(i) for i in audio_labels]
            audio_labels = np.array(audio_labels)
            y = tf.keras.utils.to_categorical(audio_labels,num_classes = 10, dtype ="int32")
            
            if os.path.exists(self.config.features_path):
                np.savez_compressed(os.path.join(self.config.features_path, "MusicFeatures.npz"), spec= spec, mel= mel_spec, mfcc= mfcc, zcr= zcr, cen= spec_c, chroma= chr, target=y)
                logger.info(f"Features extracted and saved successfully at {self.config.features_path}")
            else:
                logger.error(f"Error : Given file path does not exist -> {self.config.features_path}")
                
        except Exception as e:
            raise e

