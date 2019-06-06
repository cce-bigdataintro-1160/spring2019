import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split

np.warnings.filterwarnings('ignore')

titanic = pd.read_csv('data/heart.csv')
test = pd.read_csv('data/heart.csv')

# Applying ML Model
X = titanic.drop('Survived', axis=1)
y = titanic['Survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.40)

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
lr.fit(X_train, y_train)

predicted_values = lr.predict(X_test)

from sklearn.metrics import f1_score
print('Overall f1-score')
print(f1_score(y_test, predicted_values, average="macro"))

print('Coefficients')
print(pd.DataFrame(lr.coef_, columns=X.columns).to_string())

