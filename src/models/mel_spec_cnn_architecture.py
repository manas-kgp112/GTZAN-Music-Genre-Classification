# Standard library imports
import os
import tensorflow as tf
from tensorflow import keras


# Custom logging module
from src.logging import logger


'''
    This script contains the complete architecture of the Convolutional Network used for
    training the mel spectrogram's extracted feaures from the audio dataset.

'''



# Convolutional Neural Network Architecture

class CNN_mel_spec:
    def __init__(self, input_shape):
        self.input_shape = input_shape

    def model(self):
        model = keras.models.Sequential()
        model.add(keras.layers.Conv2D(8, (3,3), activation= 'relu', input_shape= self.input_shape, padding= 'same'))
        model.add(keras.layers.MaxPooling2D((4,4), padding= 'same'))
        model.add(keras.layers.Conv2D(16, (3,3), activation= 'relu', padding= 'same'))
        model.add(keras.layers.MaxPooling2D((4,4), padding= 'same'))
        model.add(keras.layers.Conv2D(32, (3,3), activation= 'relu', padding= 'same'))
        model.add(keras.layers.MaxPooling2D((4,4), padding= 'same'))
        model.add(keras.layers.Conv2D(64, (3,3), activation= 'relu', padding= 'same'))
        model.add(keras.layers.MaxPooling2D((4,4), padding= 'same'))
        model.add(keras.layers.Conv2D(64, (3,3), activation= 'relu', padding= 'same'))
        model.add(keras.layers.MaxPooling2D((4,4), padding= 'same'))
        model.add(keras.layers.Flatten())
        model.add(keras.layers.Dense(64, activation= 'relu'))
        model.add(keras.layers.Dense(10, activation= 'softmax'))

        return model
    

    def compiled_model(self):
        model = self.model()
        model.compile(optimizer = 'Adam', loss = 'categorical_crossentropy')

        return model