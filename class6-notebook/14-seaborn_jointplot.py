#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns

df = pd.read_csv('data/iris/iris-encoded.data',
                 sep=',',
                 header=0)

df.columns=['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)', 'class']


os.makedirs('plots/14-seaborn_jointplot', exist_ok=True)

sns.set()

plt.figure()
sns.jointplot('sepal length (cm)', 'petal length (cm)', data=df)
plt.savefig('plots/14-seaborn_jointplot/bmi__charges_jointplot.png')

plt.figure()
sns.jointplot('sepal length (cm)', 'petal length (cm)', data=df, kind='reg')
plt.savefig('plots/14-seaborn_jointplot/bmi__charges_jointplot_reg.png')

plt.figure()
sns.jointplot('sepal length (cm)', 'petal length (cm)', data=df, kind='hex')
plt.savefig('plots/14-seaborn_jointplot/bmi__charges_jointplot_hex.png')

plt.figure()
sns.jointplot('sepal length (cm)', 'petal length (cm)', data=df, kind='kde')
plt.savefig('plots/14-seaborn_jointplot/bmi__charges_jointplot_kde.png')

plt.close()
