# -*- coding: utf-8 -*-
# Created by 0138695 on 2017/4/7
from sklearn import datasets

# 读取iris数据集
iris = datasets.load_iris()
# 获取数据集中的属性值（花瓣和萼片长度宽度）
iris_X = iris.data
# 获取数据集中的标签，分别是哪种花
iris_y = iris.target

print(iris_X[::50])
print(iris_y[::50])