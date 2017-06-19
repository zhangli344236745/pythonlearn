# -*- coding: utf-8 -*-
# Created by 0138695 on 2017/6/19
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD
from keras.utils import np_utils

# Generate dummy data
import numpy as np
x_train = np.random.random((1000, 20))
y_train = np_utils.to_categorical(np.random.randint(10, size=(1000, 1)), nb_classes=10)
x_test = np.random.random((100, 20))
y_test = np_utils.to_categorical(np.random.randint(10, size=(100, 1)), nb_classes =10)

model = Sequential()
# Dense(64) is a fully-connected layer with 64 hidden units.
# in the first layer, you must specify the expected input data shape:
# here, 20-dimensional vectors.
model.add(Dense(64, activation='relu', input_dim=20))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy',
              optimizer=sgd,
              metrics=['accuracy'])
model.fit(x_train, y_train,
          nb_epoch=20,
          batch_size=128)
score = model.evaluate(x_test, y_test, batch_size=128)