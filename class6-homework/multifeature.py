#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import os
import itertools

df = pd.read_csv('data/diabetes.data',
                 sep='\s+',
                 header=0)

os.makedirs('plots', exist_ok=True)

plt.style.use("ggplot")

for col1, col2, col3, col4 in list(itertools.combinations(df.columns, 4)):
    fig, axes = plt.subplots(1, 1, figsize=(4, 4))
    axes.scatter(df[col1], df[col2], label=f'{col1} to {col2}', c=df[col3], s=df[col4]*3, marker='o',
                 alpha=0.4, edgecolors='gold', cmap='inferno')
    axes.set_title(f'{col1} to {col2} (color is {col3}, size is {col4})')
    axes.set_xlabel(col1)
    axes.set_ylabel(col2)
    axes.legend()
    plt.savefig(f'plots/boston_{col1}_{col2}_{col3}_{col4}_scatter.png', dpi=300)
    plt.close(fig)

plt.close()
