import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report

class NaiveBayes:
    def fit(self, X, y):
        self.classes = np.unique(y)
        self.mean = np.array([X[y == c].mean(0) for c in self.classes])
        self.var = np.array([X[y == c].var(0) for c in self.classes])
        self.priors = np.array([np.mean(y == c) for c in self.classes])

    def predict(self, X):
        return np.array([self._predict(x) for x in X])

    def _predict(self, x):
        probs = []
        for i in range(len(self.classes)):
            likelihood = -0.5 * np.sum(np.log(2 * np.pi * self.var[i]))
            likelihood -= np.sum((x - self.mean[i]) ** 2 / (2 * self.var[i]))
            probs.append(np.log(self.priors[i]) + likelihood)
        return self.classes[np.argmax(probs)]

if __name__ == '__main__':
    iris = load_iris()
    X, y = iris.data, iris.target
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=1)

    nb = NaiveBayes()
    nb.fit(Xtr, ytr)

    y_pred = nb.predict(Xte)

    print("Accuracy: %.4f" % np.mean(y_pred == yte))
    print("Predictions:", iris.target_names[y_pred])
    print("\nConfusion Matrix:")
    print(confusion_matrix(yte, y_pred))
    print("\nClassification Report:")
    print(classification_report(yte, y_pred, target_names=iris.target_names))
