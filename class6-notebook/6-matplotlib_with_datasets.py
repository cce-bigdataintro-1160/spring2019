#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

df = pd.read_csv('data/boston/housing.data',
                 sep='\s+',
                 header=None)

df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

sorted_by_medv_df = df.sort_values('MEDV')

fig, axes = plt.subplots(2, 1, figsize=(5, 5))

axes[0].plot(sorted_by_medv_df['MEDV'], sorted_by_medv_df['CRIM'], label='Crime', color='purple', linestyle='-.',
             linewidth=0.2)
axes[0].set_title('Crime vs Value')
axes[0].set_xlabel('Value')
axes[0].set_ylabel('Crime')
axes[0].legend()

axes[1].scatter(df['MEDV'], df['CRIM'], s=2, label='Crime', color='brown', marker='*')
axes[1].set_title('Crime vs Value')
axes[1].set_xlabel('Value')
axes[1].set_ylabel('Crime')
axes[1].legend()

os.makedirs('plots/6-matplotlib_with_datasets', exist_ok=True)

plt.savefig('plots/6-matplotlib_with_datasets/boston_crime_scatter.png', dpi=300)

plt.close()