import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

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
X_train, X_test, y_train, y_test = train_test_split(scaled_features, y, test_size=0.35)

f1_scores = []
error_rate = []

# Creating one model for each n neighbors, predicting and storing the result in an array
for i in range(1, 100):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    y_predicted = knn.predict(X_test)
    f1_scores.append(f1_score(y_test, y_predicted, average="macro"))
    error_rate.append(np.mean(y_predicted != y_test))


# Plotting results
plt.plot(f1_scores, color='green', label='f1 score', linestyle='--')
plt.plot(error_rate, color='red', label='error rate', linestyle='--')
plt.xlabel('n neighbors parameter')
plt.ylabel('f1_score/error_rate')
plt.legend()
plt.show()



