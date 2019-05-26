#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns

df = pd.read_csv('data/iris/iris-encoded.data',
                 sep=',',
                 header=0)

df.columns = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)', 'class']

os.makedirs('plots/10-seaborn_plots', exist_ok=True)

sns.set()

sorted_by_sepal_length_df = df.sort_values('sepal length (cm)')

sns.lineplot('sepal length (cm)', 'petal length (cm)', data=sorted_by_sepal_length_df)
sns.lineplot('sepal length (cm)', 'petal width (cm)', data=sorted_by_sepal_length_df)
plt.legend(['sepal length (cm) vs petal length (cm)', 'petal length (cm) vs petal width (cm)'])
plt.savefig('plots/10-seaborn_plots/iris_sepal length_petal length_lineplot.png')
plt.clf()

sns.scatterplot('sepal length (cm)', 'petal length (cm)', data=df)
plt.legend(['sepal length (cm)'])
plt.savefig('plots/10-seaborn_plots/iris_sepal length_petal length_scatterplot.png')

