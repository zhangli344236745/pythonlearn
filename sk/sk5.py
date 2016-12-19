__author__ = '0138695'

from sklearn import datasets
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

loaded_data = datasets.load_boston()
data_X = loaded_data.data
#print data_X
data_Y = loaded_data.target
#print data_Y

model = LinearRegression()
model.fit(data_X,data_Y)
print data_X[:4,:]
print model.predict(data_X[:4,:])
print data_Y[:4]

X,Y = datasets.make_regression(n_samples=100, n_features=1, n_targets=1, noise=50)
plt.scatter(X,Y)
plt.show()
