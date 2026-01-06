import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
from collections import Counter

def knn_predict(Xtr, ytr, Xte, k=3):
    preds = []
    for x in Xte:
        dists = np.linalg.norm(Xtr - x, axis=1)
        k_labels = ytr[np.argsort(dists)[:k]]
        preds.append(Counter(k_labels).most_common(1)[0][0])
    return np.array(preds)

if __name__ == '__main__':
    iris = load_iris()
    X, y = iris.data, iris.target
    class_names = iris.target_names

    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=1)

    y_pred = knn_predict(Xtr, ytr, Xte, k=3)

    print("Accuracy: %.4f" % np.mean(y_pred == yte))
    print("Predictions:", class_names[y_pred])
    print("\nConfusion Matrix:")
    print(confusion_matrix(yte, y_pred))
    print("\nClassification Report:")
    print(classification_report(yte, y_pred))
