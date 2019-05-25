#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv('data/diabetes.data',
                 sep='\s+',
                 header=0)

os.makedirs('plots/7-matplotlib_dataset_exploration', exist_ok=True)

for col1_idx, column1 in enumerate(df.columns):
    for col2_idx, column2 in enumerate(df.columns):
        if col1_idx < col2_idx:
            fig, axes = plt.subplots(1, 1, figsize=(5, 5))
            axes.scatter(df[column1], df[column2], label=f'{column1} to {column2}', color='green', marker='x')
            axes.set_title(f'{column1} to {column2}')
            axes.set_xlabel(column1)
            axes.set_ylabel(column2)
            axes.legend()
            plt.savefig(f'plots/7-matplotlib_dataset_exploration/diabetes_{column1}_{column2}_scatter.png', dpi=300)
            plt.close(fig)

plt.close()
