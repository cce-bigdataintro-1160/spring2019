#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns

df = pd.read_csv('data/iris/iris-encoded.data',
                 sep=',',
                 header=0)

df.columns = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)', 'class']

os.makedirs('plots/14-seaborn_jointplot', exist_ok=True)

sns.set()

for jointplot_kind in ['reg', 'hex', 'kde', 'scatter']:
    sns.jointplot('sepal length (cm)', 'petal length (cm)', data=df, kind=jointplot_kind)
    plt.savefig(f'plots/14-seaborn_jointplot/iris_sepal length (cm) to petal length (cm)_jointplot_{jointplot_kind}.png')
    plt.clf()

plt.close()
