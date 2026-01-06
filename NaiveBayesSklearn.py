import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

iris = load_iris()
X, y = iris.data, iris.target

Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=1)

nb = GaussianNB()
nb.fit(Xtr, ytr)

y_pred = nb.predict(Xte)

print("Accuracy: %.4f" % accuracy_score(yte, y_pred))
print("Predictions:", iris.target_names[y_pred])
print("\nConfusion Matrix:\n", confusion_matrix(yte, y_pred))
print("\nClassification Report:\n", classification_report(yte, y_pred, target_names=iris.target_names))
