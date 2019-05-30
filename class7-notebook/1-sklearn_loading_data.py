import pandas as pd
import numpy as np
import seaborn as sns

# Loading data using our pandas DataFrames (as in all previous classes)
wine_df = pd.read_csv('data/wine.data',
                      sep=',',
                      header=0)
wine_df.columns = ['class', 'alcohol', 'malic_acid', 'ash', 'alcalinity_of_ash', 'magnesium', 'total_phenols',
                   'flavanoids',
                   'nonflavanoid_phenols', 'proanthocyanins', 'color_intensity', 'hue', 'od280 od315_of_diluted_wines',
                   'proline']

X = wine_df.drop('class', axis=1)
y = wine_df['class']

print(X.shape)
print(y.shape)

# Loading data using sklearn toys datasets
from sklearn.datasets import load_wine

# Checking the dataset content
wine = load_wine()
print(wine.keys())
print(wine.data)
print(wine.target)
print(wine.feature_names)

X = wine.data
y = wine.target

print(X.shape)
print(y.shape)

# Rebuilding pandas DF from dataset (for plotting and statistical facts)
convert_to_df = pd.DataFrame(data=np.c_[wine.data, wine.target], columns=wine.feature_names + ['target'])
sns.pairplot(convert_to_df)
print(convert_to_df.describe())




