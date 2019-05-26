#!/usr/bin/env python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns

df = pd.read_csv('data/breast-cancer/wdbc.data',
                 sep=',',
                 header=0)

df.columns = ['id', 'diagnosis', 'mean radius', 'mean texture', 'mean perimeter', 'mean area',
              'mean smoothness', 'mean compactness', 'mean concavity',
              'mean concave points', 'mean symmetry', 'mean fractal dimension',
              'radius error', 'texture error', 'perimeter error', 'area error',
              'smoothness error', 'compactness error', 'concavity error',
              'concave points error', 'symmetry error', 'fractal dimension error',
              'worst radius', 'worst texture', 'worst perimeter', 'worst area',
              'worst smoothness', 'worst compactness', 'worst concavity',
              'worst concave points', 'worst symmetry', 'worst fractal dimension']

df.drop('id', axis=1, inplace=True)

os.makedirs('plots/12-seaborn_categorical_1', exist_ok=True)

sns.set()
sns.set_style('white')  # ticks, darkgrid, whitegrid

df['encoded_diagnosis'] = df['diagnosis'].map({'B': 0, 'M': 1})

sns.countplot('encoded_diagnosis', data=df)
plt.savefig('plots/12-seaborn_categorical_1/cancer_encoded_diagnosis_countplot.png')
plt.clf()

sns.barplot('encoded_diagnosis', 'mean area', data=df, estimator=np.mean)
plt.savefig('plots/12-seaborn_categorical_1/cancer_encoded_diagnosis_mean area_countplot.png')
plt.clf()

sns.boxplot('encoded_diagnosis', 'mean area', data=df, palette='inferno')
plt.savefig('plots/12-seaborn_categorical_1/cancer_encoded_diagnosis_mean area_boxplot.png')

plt.close()
