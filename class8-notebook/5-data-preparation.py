import pandas as pd
import numpy as np

np.warnings.filterwarnings('ignore')

titanic = pd.read_csv('data/titanic/train.csv')

# Overall exploration before cleanup
print('\n\n********************************** Dataset BEFORE Cleanup ***************************************')
print(titanic.info())
print(titanic.head(5).to_string())

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

# Prepared dataset overall exploration
print('\n\n********************************** Dataset AFTER Cleanup ***************************************')
print(titanic.info())
print(titanic.head(5).to_string())
