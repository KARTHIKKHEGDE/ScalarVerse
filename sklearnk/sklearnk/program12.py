import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

if __name__ == '__main__':
    iris = load_iris()
    X = iris.data

    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    labels = kmeans.fit_predict(X)
    centroids = kmeans.cluster_centers_

    colors = ['r','g','b']

    for i in range(3): plt.scatter(X[labels==i,0], X[labels==i,1], c=colors[i], label=f'Cluster {i+1}')
    plt.scatter(centroids[:,0], centroids[:,1], c='black', marker='x', s=100, label='Centroids')
    plt.xlabel('Sepal Length'); plt.ylabel('Sepal Width'); plt.title('K-Means Clustering on Iris Dataset')
    plt.legend(); plt.show()
