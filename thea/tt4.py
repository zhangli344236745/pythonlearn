# -*- encoding: utf-8 -*-
import numpy as np

def createData():
    data_set = np.array([[3, 104], [2, 200], [1, 81], [101, 10], [99, 5], [98, 2]])
    labels = ['爱情片', '爱情片', '爱情片', '动作片', '动作片', '动作片']
    return data_set, labels

def knn(inx,dataSet,labels,k):
    data_size = dataSet.shape[0]
    diff = np.tile(inx, (data_size, 1)) - dataSet
    sqDiff = diff**2
    distance = sqDiff.sum(axis=1)**0.5
    sortIndex = np.argsort(distance)
    print sortIndex
    classCount = {}
    for i in xrange(k):
        voteLabels = labels[sortIndex[i]]
        classCount[voteLabels]  = classCount.get(voteLabels, 0) + 1
    print classCount
    result = sorted(classCount.iteritems(),key=lambda d:d[1], reverse=True)
    return result[0][0]

if __name__ == '__main__':
    dataSet, labels = createData()
    result = knn([18, 90], dataSet, labels, 4)
    print result