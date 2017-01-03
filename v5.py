import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets.samples_generator import make_blobs

X, y = make_blobs(n_samples=10000, n_features=3, centers=[[3,3, 3], [0,0,0], [1,1,1], [2,2,2]], cluster_std=[0.2, 0.1, 0.2, 0.2],
                  random_state =9)
# fig = plt.figure()
# ax = Axes3D(fig, rect=[0, 0, 1, 1], elev=30, azim=20)
# plt.scatter(X[:, 0], X[:, 1], X[:, 2])
# plt.show()

from sklearn.decomposition import PCA
pca = PCA(n_components=1)
pca.fit(X)
print pca.explained_variance_ratio_
print pca.explained_variance_

X_new = pca.transform(X)
print X_new
plt.scatter(X_new[:, 0], X_new[:, 1],marker='o')
plt.show()