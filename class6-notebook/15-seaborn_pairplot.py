#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns

os.makedirs('plots/15-seaborn_pairplot', exist_ok=True)

#darkgrid, whitegrid, dark, white, ticks
sns.set(style='darkgrid', palette='coolwarm')

#Diabetes Pairplot
diabetes_df = pd.read_csv('data/diabetes.data',
                          sep='\s+',
                          header=0)
sns.pairplot(diabetes_df, hue='SEX', diag_kind='hist')
plt.savefig('plots/15-seaborn_pairplot/diabetes_pairplot.png')
plt.clf()

# Boston Pairplot
boston_df = pd.read_csv('data/boston/housing.data',
                        sep='\s+',
                        header=None)
boston_df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT',
                     'MEDV']
sns.pairplot(boston_df, hue='CHAS', diag_kind='hist')
plt.savefig('plots/15-seaborn_pairplot/boston_pairplot.png')
plt.clf()

# Cancer Pairplot
cancer_df = pd.read_csv('data/breast-cancer/wdbc.data',
                        sep=',',
                        header=0)
cancer_df.columns = ['id', 'diagnosis', 'mean radius', 'mean texture', 'mean perimeter', 'mean area',
                     'mean smoothness', 'mean compactness', 'mean concavity',
                     'mean concave points', 'mean symmetry', 'mean fractal dimension',
                     'radius error', 'texture error', 'perimeter error', 'area error',
                     'smoothness error', 'compactness error', 'concavity error',
                     'concave points error', 'symmetry error', 'fractal dimension error',
                     'worst radius', 'worst texture', 'worst perimeter', 'worst area',
                     'worst smoothness', 'worst compactness', 'worst concavity',
                     'worst concave points', 'worst symmetry', 'worst fractal dimension']
cancer_df['encoded_diagnosis'] = cancer_df['diagnosis'].map({'B': 0, 'M': 1})
sns.pairplot(cancer_df, hue='encoded_diagnosis', diag_kind='hist')
plt.savefig('plots/15-seaborn_pairplot/cancer_pairplot.png')
plt.clf()


#Iris Pairplot
iris_df = pd.read_csv('data/iris/iris-encoded.data',
                      sep=',',
                      header=0)
iris_df.columns = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)', 'class']
sns.pairplot(iris_df, hue='class', diag_kind='hist')
plt.savefig('plots/15-seaborn_pairplot/iris_pairplot.png')
plt.clf()


# Wine Pairplot
wine_df = pd.read_csv('data/wine.data',
                      sep=',',
                      header=0)
wine_df.columns = ['class', 'alcohol', 'malic_acid', 'ash', 'alcalinity_of_ash', 'magnesium', 'total_phenols',
                   'flavanoids',
                   'nonflavanoid_phenols', 'proanthocyanins', 'color_intensity', 'hue', 'od280 od315_of_diluted_wines',
                   'proline']
sns.pairplot(wine_df, hue='class', diag_kind='hist')
plt.savefig('plots/15-seaborn_pairplot/wine_pairplot.png')

plt.close()
