# -*- coding: utf-8 -*-
# Created by 0138695 on 2017/2/17
from keras.layers import Convolution2D,MaxPooling2D,Activation
from keras.models import Sequential
import cv2
import matplotlib.pyplot as plt
import numpy as np


cat = cv2.imread("./cat.png")
plt.imshow(cat)
#plt.show()
print cat.shape

model = Sequential()
model.add(Convolution2D(3,3,3,input_shape=cat.shape))

#cat_batch = np.expand_dims(cat,axis=0)
#conv_cat = model.predict(cat_batch)

def visualize_cat(model, cat,plt):
    # Keras expects batches of images, so we have to add a dimension to trick it into being nice
    cat_batch = np.expand_dims(cat,axis=0)
    conv_cat = model.predict(cat_batch)
    conv_cat = np.squeeze(conv_cat, axis=0)
    print conv_cat.shape
    plt.imshow(conv_cat)
    #plt.show()


visualize_cat(model,cat,plt)