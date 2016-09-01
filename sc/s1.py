# -*- coding:utf-8 -*-

from sklearn import tree

feateures = [[140,1],[130,1],[150,0],[170,0]]
labels = [0,0,1,1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(feateures,labels)
print(clf.predict([[150,0]]))
