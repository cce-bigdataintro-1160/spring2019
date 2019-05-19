#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns


df = pd.read_csv('data/iris/iris-encoded.data',
                 sep=',',
                 header=0)

df.columns=['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)', 'class']

os.makedirs('plots/10-seaborn_plots', exist_ok=True)

sns.set()

sorted_by_sepal_length_df = df.sort_values('sepal length (cm)')

plt.figure()
sns.lineplot('sepal length (cm)', 'petal length (cm)', data=sorted_by_sepal_length_df)
plt.savefig('plots/10-seaborn_plots/sepal length_petal length_lineplot.png')

plt.figure()
sns.scatterplot('sepal length (cm)', 'petal length (cm)', data=df)
plt.savefig('plots/10-seaborn_plots/sepal length_petal length_scatterplot.png')

plt.figure()
sns.scatterplot('sepal length (cm)', 'sepal width (cm)', data=df)
plt.savefig('plots/10-seaborn_plots/sepal length_sepal width_scatterplot.png')

plt.close()
