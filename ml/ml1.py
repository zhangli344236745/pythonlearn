# -*- coding: utf-8 -*-
# Created by 0138695 on 2017/3/13
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

n_classses = 3
plot_colors = 'bry'
plot_step = 0.02

iris = load_iris()

# 鸢尾花数据有4个属性，取两两属性为一组，遍历
for pairidx, pair in enumerate([[0, 1], [0, 2], [0, 3],
                                [1, 2], [1, 3], [2, 3]]):
	X = iris.data[:, pair]
	y = iris.target

	clf = DecisionTreeClassifier().fit(X, y)
	plt.subplot(2, 3, pairidx + 1)
	x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
	y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
	xx, yy = np.meshgrid(np.arange(x_min, x_max, plot_step),
	                     np.arange(y_min, y_max, plot_step))
	# 使用分类器计算每个坐标点的分类，并绘制分类结果矩阵的等高线
	Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
	Z = Z.reshape(xx.shape)
	cs = plt.contourf(xx, yy, Z, cmap=plt.cm.Paired)

	# 使用属性特征名作为横纵坐标名
	plt.xlabel(iris.feature_names[pair[0]])
	plt.ylabel(iris.feature_names[pair[1]])
	plt.axis("tight")

	# 绘制训练数据点，并用不同颜色区分
	for i, color in zip(range(n_classes), plot_colors):
		idx = np.where(y == i)
		plt.scatter(X[idx, 0], X[idx, 1], c=color, label=iris.target_names[i],
		            cmap=plt.cm.Paired)

	plt.axis("tight")

plt.suptitle("Decision surface of a decision tree using paired features")
plt.legend()
plt.show()