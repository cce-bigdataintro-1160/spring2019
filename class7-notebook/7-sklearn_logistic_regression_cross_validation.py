from sklearn.datasets import load_iris

iris = load_iris()
columns_names = iris.feature_names
y = iris.target
X = iris.data

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()

# Cross validation using cross_val_score
from sklearn.model_selection import cross_val_score, ShuffleSplit
print(cross_val_score(lr, X, y, cv=5))

# Cross validation using shuffle split
cv = ShuffleSplit(n_splits=5)
print(cross_val_score(lr, X, y, cv=cv))
