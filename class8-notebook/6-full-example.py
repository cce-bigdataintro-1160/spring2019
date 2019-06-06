import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split

np.warnings.filterwarnings('ignore')

titanic = pd.read_csv('data/titanic/train.csv')
test = pd.read_csv('data/titanic/test.csv')

# Filling up the missing data with the most common values
titanic['Age'] = titanic['Age'].fillna(value=titanic['Age'].mean())
titanic['Embarked'] = titanic['Embarked'].fillna(value='S')

# Encoding categorical variables using dummy variables
encoded_sex = pd.get_dummies(titanic['Sex'], drop_first=True)
encoded_embarked = pd.get_dummies(titanic['Embarked'], drop_first=True)
titanic = pd.concat([titanic, encoded_sex, encoded_embarked], axis=1)

# Transforming the Cabin field information in numerical information
titanic['MarkedCabin'] = titanic['Cabin'].apply(lambda x: 0 if type(x) == float else 1)

# Removing non numerical and 'noise' columns
titanic.drop(['PassengerId', 'Sex', 'Embarked', 'Name', 'Ticket', 'Cabin'], axis=1, inplace=True)

# Prepared dataset overall plotting
plt.figure(figsize=(8, 8))
sns.pairplot(titanic, diag_kind='hist', hue='Survived')
plt.savefig('titanic_clean.png')

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

