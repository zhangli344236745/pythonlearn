import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.optimizers import SGD
from keras.utils import np_utils    
from keras.utils.visualize_util import plot


def run():
    model = Sequential()
    model.add(Dense(4, input_dim=2, init='uniform'))
    model.add(Activation('relu'))
    model.add(Dense(2, init='uniform'))
    model.add(Activation('sigmoid'))
    sgd = SGD(lr=0.05, decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(loss='binary_crossentropy', optimizer=sgd, metrics=['accuracy'])
    plot(model, to_file='model.png')

if __name__ == '__main__':
    run()