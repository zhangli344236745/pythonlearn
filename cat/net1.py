# -*- coding: utf-8 -*-
# Created by 0138695 on 2017/2/17
import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
	a = []
	for item in x:
		a.append(1/(1+np.exp(-item)))
	return a

x = np.arange(-6.0,6.0,0.2)
sig = sigmoid(x)
plt.plot(x,sig)
plt.grid()
plt.show()