from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
columns_names = iris.feature_names
y = iris.target
X = iris.data

# Splitting features and target datasets into: train and test
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35)

# Training a Linear Regression model with fit()
from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()
lr.fit(X_train, y_train)

# Output of the training is a model: a + b*X0 + c*X1 + d*X2 ...
print(f"Intercept per class: {lr.intercept_}\n")
print(f"Coeficients per class: {lr.coef_}\n")

print(f"Available classes: {lr.classes_}\n")
print(f"Named Coeficients for class 1: {pd.DataFrame(lr.coef_[0], columns_names)}\n")
print(f"Named Coeficients for class 2: {pd.DataFrame(lr.coef_[1], columns_names)}\n")
print(f"Named Coeficients for class 3: {pd.DataFrame(lr.coef_[2], columns_names)}\n")

print(f"Number of iterations generating model: {lr.n_iter_}")
