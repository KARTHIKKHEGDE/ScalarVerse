from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Load Iris dataset
iris = load_iris()

# Use all features
X = iris.data
y_original = iris.target

# Binary classification: Setosa vs Others
y = (y_original != 0).astype(int)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.4, random_state=9
)

# Create Naive Bayes model
model = GaussianNB()

# Train the model
model.fit(X_train, y_train)

# ---------------- USER INPUT ----------------
print("\nEnter flower details for prediction:")

sepal_length = float(input("Sepal Length (in cm): "))
sepal_width  = float(input("Sepal Width (in cm): "))
petal_length = float(input("Petal Length (in cm): "))
petal_width  = float(input("Petal Width (in cm): "))

user_input = [[sepal_length, sepal_width, petal_length, petal_width]]

# Prediction
prediction = model.predict(user_input)

# Output class name
if prediction[0] == 0:
    print("\nPredicted Class: Setosa")
else:
    print("\nPredicted Class: Not Setosa (Versicolor / Virginica)")

# ---------------- MODEL ACCURACY ----------------
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("\nModel Accuracy:", accuracy)
