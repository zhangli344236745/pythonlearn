__author__ = '0138695'
import random
from scipy.spatial import distance
import os

def euc(a,b):
    return distance.euclidean(a,b)

class ScrappyKNN:
    def __init__(self):
        pass

    def fit(self,x_trian,y_train):
        self.x_train = x_trian
        self.y_train = y_train

    def predict(self,x_test):
        predictions = []
        for row in x_test:
            label = self.closest(row)
            predictions.append(label)
        return predictions

    def closest(self,row):
        best_dist = euc(row, self.x_train[0])
        best_index = 0
        for i in range(1, len(self.x_train)):
            dist = euc(row, self.x_train[i])
            if dist < best_dist:
                best_dist = dist
                best_index = i
        return self.y_train[best_index]

from sklearn import datasets
from sklearn.cross_validation import train_test_split

iris = datasets.load_iris()
X = iris.data
Y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=.5)
my_classifier = ScrappyKNN()

my_classifier.fit(X_train, y_train)

predictions = my_classifier.predict(X_test)
print(predictions)

from sklearn.metrics import accuracy_score

print accuracy_score(y_test, predictions)

