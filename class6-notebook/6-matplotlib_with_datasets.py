#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

df = pd.read_csv('data/boston/housing.data',
                 sep='\s+',
                 header=None)

df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

fig, axes = plt.subplots(1, 1, figsize=(5, 5))

axes.scatter(df['MEDV'], df['CRIM'], s=2, label='Crime', color='brown', marker='*')
axes.set_title('Crime vs Value')
axes.set_xlabel('Value')
axes.set_ylabel('Crime')
axes.legend()

os.makedirs('plots/6-matplotlib_with_datasets', exist_ok=True)

plt.savefig('plots/6-matplotlib_with_datasets/boston_crime_value_scatter.png', dpi=300)

plt.close()













# Plotting two vars with line
# sorted_by_medv_df = df.sort_values('MEDV')
# fig, axes = plt.subplots(1, 1, figsize=(5, 5))
# axes.plot(sorted_by_medv_df['MEDV'], sorted_by_medv_df['CRIM'], label='Crime', color='purple')
# axes.set_title('Crime vs Value')
# axes.set_xlabel('Value')
# axes.set_ylabel('Crime')
# axes.legend()
# plt.savefig('plots/6-matplotlib_with_datasets/boston_crime_value_line.png', dpi=300)