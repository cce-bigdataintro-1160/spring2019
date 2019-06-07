import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split

# 1. Choose one of the datasets above and explore the dataset webpage, read the documentation and author's proposal
# 3. Load the dataset using pandas
# 4. Print the dataframe statistical summaries looking for:
#   * Relevant variables
#   * The dimensions of the dataset
#   * Variables with empty values
#   * Variables to be cleaned, corrected or enhanced
# 5. Ask at least one question you can answer by using the dataframe filtering through predicate like:
# `df_name[df_name['Age'] > 30]`. For example, using the Spotify dataset try to find the 10 most `danceable` songs.
# 6. Use the method `df['my_column'].value_counts()` on a categorical column.
# 7. Check the correlation of the variables in your dataset!
# 8. Plot everything you need in order to understand this dataset and its correlations. You can use all the techniques we learned in the previous classes.
# 9. Finally, choose a variable to be used as target and run your classification or regression.
# 10. Check if your score is acceptable!


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

