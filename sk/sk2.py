__author__ = '0138695'
import numpy as np
from sklearn.naive_bayes import GaussianNB

X = np.array([[-1,-1],[-2,-1],[-3,-2],[1,1],[2,1],[3,2]])
Y = np.array([1,1,1,2,2,2])
clf = GaussianNB()
clf.fit(X,Y)

print "==Predict result by predict=="
print(clf.predict([[-0.8, -1]]))
print "==Predict result by predict_proba=="
print(clf.predict_proba([[-0.8, -1]]))
print "==Predict result by predict_log_proba=="
print(clf.predict_log_proba([[-0.8, -1]]))