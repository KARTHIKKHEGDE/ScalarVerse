import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.inspection import DecisionBoundaryDisplay


if __name__ == '__main__':
    # Load data
    iris = load_iris()
    X = iris.data[:, :2]
    y = (iris.target != 0).astype(int)

    # Split
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.4, random_state=9)

    # Scale
    sc = StandardScaler()
    Xtr = sc.fit_transform(Xtr)
    Xte = sc.transform(Xte)

    # Train
    lr = LogisticRegression()
    lr.fit(Xtr, ytr)

    # Accuracy
    print("Accuracy:", np.mean(lr.predict(Xte) == yte))

    # Plot decision boundary
    DecisionBoundaryDisplay.from_estimator(lr, Xtr, response_method="predict", alpha=0.3)
    plt.scatter(Xtr[:,0], Xtr[:,1], c=ytr, edgecolor="k")
    plt.xlabel("Sepal Length (scaled)")
    plt.ylabel("Sepal Width (scaled)")
    plt.title("Logistic Regression Decision Boundary")
    plt.show()
