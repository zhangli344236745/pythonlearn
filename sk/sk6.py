import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import KMeans

X ,y = make_blobs(n_samples=1000,n_features=2, centers=[[-1,-1], [0,0], [1,1], [2,2]], cluster_std=[0.4, 0.2, 0.2, 0.2],
                  random_state =9)

plt.scatter(X[:,0],X[:,1],marker='o')
plt.show()

y_pred = KMeans(n_clusters=2,random_state=9).fit_predict(X)
plt.scatter(X[:,0],X[:,1],c=y_pred)
plt.show()
