import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

if __name__ == '__main__':
    # Load Iris dataset
    iris = load_iris()
    X = iris.data

    # Apply K-Means
    kmeans = KMeans(n_clusters=3, random_state=42)
    labels = kmeans.fit_predict(X)
    centroids = kmeans.cluster_centers_

    # Plot clusters one by one to add labels
    plt.scatter(X[labels == 0, 0], X[labels == 0, 1], label="Cluster 1")
    plt.scatter(X[labels == 1, 0], X[labels == 1, 1], label="Cluster 2")
    plt.scatter(X[labels == 2, 0], X[labels == 2, 1], label="Cluster 3")

    # Plot centroids
    plt.scatter(
        centroids[:, 0], centroids[:, 1],
        c='black', marker='X', s=100,
        label="Centroids"
    )

    # Labels and title
    plt.xlabel("Sepal Length")
    plt.ylabel("Sepal Width")
    plt.title("K-Means Clustering on Iris Dataset")

    # Show legend
    plt.legend()

    plt.show()
