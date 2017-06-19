# -*- coding: utf-8 -*-
# Created by 0138695 on 2017/6/19
from keras.models import Sequential
from keras.layers import Dense,Convolution2D,Flatten
import keras
import numpy as np
from keras.utils import generic_utils,np_utils
# layer = Dense(32)
# config = layer.get_config()
# rec = Dense.from_config(config)
# print rec

model = Sequential()
model.add(Convolution2D(64,3,3,border_mode='same',input_shape=(3,32,32)))
model.add(Flatten())
y_train = np_utils.to_categorical(np.random.randint(10, size=(100, 1)),nb_classes=10)

