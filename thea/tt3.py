import numpy
import theano
import theano.tensor as T
from theano import pp

x = T.dscalar('x')
y = x ** 2
gy = T.grad(y,x)
pp(gy)
f = theano.function([x], gy)
print f(4)

x = T.dmatrix('x')
s = T.sum(1/(1+T.exp(-x)))
gs = T.grad(s,x)
dlogistic = theano.function([x], gs)
print dlogistic([[0, 1], [-1, -2]])

xx = T.matrix('xx')
print((xx**2).shape)
f = theano.function([xx],(xx**2).shape)

x = T.dscalar("x")
y = T.dscalar('y')
z = x + y
print type(x)
print x.type
print T.dscalar
print x.type is T.dscalar
print pp(z)
print z.type
f = theano.function([x,y],z)
print f(1,2)

a = theano.tensor.vector()
out = a + a**3
f = theano.function([a],out)
print(f([0,1,2]))

x = T.dmatrix('x')
s = T.exp(-x)
logis = theano.function([x],s)
print(logis([[0,1000]]))