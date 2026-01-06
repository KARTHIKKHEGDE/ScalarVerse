import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

iris = load_iris()
X, y = iris.data, iris.target
class_names = iris.target_names

Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=1)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(Xtr, ytr)

y_pred = knn.predict(Xte)

print("Accuracy: %.4f" % accuracy_score(yte, y_pred))
print("Predictions:", class_names[y_pred])
print("\nConfusion Matrix:\n", confusion_matrix(yte, y_pred))
print("\nClassification Report:\n", classification_report(yte, y_pred, target_names=class_names))
