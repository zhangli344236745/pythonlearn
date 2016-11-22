__author__ = '0138695'
from keras.models import Sequential
from keras.layers import Dense,Activation

model = Sequential()
model.add(Dense(output_dim=64,input_dim=100))
model.add(Activation('relu'))
model.add(Dense(output_dim=10))
model.add(Activation('softmax'))
model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])