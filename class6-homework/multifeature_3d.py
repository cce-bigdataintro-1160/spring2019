#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import os
import itertools
from mpl_toolkits.mplot3d import Axes3D

df = pd.read_csv('data/diabetes.data',
                 sep='\s+',
                 header=0)

os.makedirs('plots/3d', exist_ok=True)

plt.style.use("ggplot")

m_df = df[df['SEX'] == 2]
f_df = df[df['SEX'] == 1]

for col0, col1, col2, col3, col4 in list(itertools.combinations(df.columns, 5)):
    fig = plt.figure(figsize=(6, 6))
    axes = fig.add_subplot(1, 1, 1, projection='3d')
    fig.suptitle(f'{col0} to {col1} to {col2} (color: {col3}, size: {col4})')

    axes.scatter(m_df[col0], m_df[col1], m_df[col2], label=f'Male', c=m_df[col3], s=m_df[col4], marker='s',
                 alpha=0.6, edgecolors='black', cmap='YlGn')
    axes.scatter(f_df[col0], f_df[col1], f_df[col2], label=f'Female', c=f_df[col3], s=f_df[col4], marker='o',
                 alpha=0.6, edgecolors='black', cmap='RdPu')

    axes.set_xlabel(col0)
    axes.set_ylabel(col1)
    axes.set_zlabel(col2)
    axes.legend()
    plt.savefig(f'plots/3d/boston_{col0}_{col1}_{col2}_{col3}_{col4}_scatter.png', dpi=300)
    plt.close(fig)

plt.close()

