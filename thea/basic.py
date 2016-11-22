from __future__ import print_function

import numpy as np
import theano.tensor as T
from theano import function

x = T.dscalar('x')
y = T.dscalar('y')

z = x+y
f = function([x,y],z)
print(f(2,3))

x = T.dmatrix('x')
y = T.dmatrix('y')

z = x+y
f = function([x,y],z)
a = np.arange(12).reshape((3,4))
b = 10 * np.ones((3,4))
print(a)
print(b)
print(f(a,b))

x = T.dmatrix('x')
s = 1 / (1 + T.exp(-x))    # logistic or soft step
logistic = function([x], s)
print(logistic([[0, 1],[-1, -2]]))