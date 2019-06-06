import warnings
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import GaussianNB

warnings.filterwarnings("ignore")

# Load wine dataset
wine = load_wine()
columns_names = wine.feature_names
y = wine.target
X = wine.data

# Scaling data (KNeighbors methods do not scale automatically!)
scaler = StandardScaler()
scaler.fit(X)
scaled_features = scaler.transform(X)

# Splitting dataset
X_train, X_test, y_train, y_test = train_test_split(scaled_features, y, test_size=0.35, random_state=1)

f1_scores = []
error_rate = []

# Creating one model for each n neighbors, predicting and storing the result in an array
for Estimator in [KNeighborsClassifier, LogisticRegression, SGDClassifier, GaussianNB]:
    estimator = Estimator()
    estimator.fit(X_train, y_train)
    y_predicted = estimator.predict(X_test)
    f1 = f1_score(y_test, y_predicted, average="macro")
    error = np.mean(y_predicted != y_test)
    f1_scores.append(f1)
    error_rate.append(error)
    print(f'For {type(estimator)} the f1-score is {f1} and error rate is {error}')

# Plotting results
plt.plot(f1_scores, color='green', label='f1 score', linestyle='--')
plt.plot(error_rate, color='red', label='error rate', linestyle='--')
plt.xlabel('n neighbors parameter')
plt.ylabel('f1_score/error_rate')
plt.xticks(np.arange(4), ['KNeighborsClassifier', 'LogisticRegression', 'SGDClassifier', 'GaussianNB'])
plt.legend()
plt.show()




