import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


# Sigmoid
def sigmoid(z):
    return 1 / (1 + np.exp(-z))


# Logistic Regression
def train(X, y, lr=0.001, iters=200):
    w = np.zeros(X.shape[1])
    for _ in range(iters):
        w -= lr * (X.T @ (sigmoid(X @ w) - y)) / len(y)
    return w


if __name__ == '__main__':
    # Load data
    iris = load_iris()
    X = iris.data[:, :2]    
    y = (iris.target != 0).astype(int)

    # Split & scale
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.4, random_state=9)
    sc = StandardScaler()
    Xtr = sc.fit_transform(Xtr)
    Xte = sc.transform(Xte)

    # Train
    w = train(Xtr, ytr)

    # Accuracy
    pred = sigmoid(Xte @ w) > 0.5
    print("Accuracy:", np.mean(pred == yte))

    # Plot decision boundary
    xx, yy = np.meshgrid(
        np.arange(Xtr[:,0].min()-1, Xtr[:,0].max()+1, 0.1),
        np.arange(Xtr[:,1].min()-1, Xtr[:,1].max()+1, 0.1)
    )

    Z = sigmoid(np.c_[xx.ravel(), yy.ravel()] @ w) > 0.5
    plt.contourf(xx, yy, Z.reshape(xx.shape), alpha=0.4)
    plt.scatter(Xtr[:,0], Xtr[:,1], c=ytr)
    plt.xlabel("Sepal length")
    plt.ylabel("Sepal width")
    plt.title("Logistic Regression")
    plt.show()
