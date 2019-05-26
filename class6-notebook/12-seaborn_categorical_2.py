#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns

os.makedirs('plots/12-seaborn_categorical_2', exist_ok=True)

sns.set(style='white')# ticks, darkgrid, whitegrid

boston_df = pd.read_csv('data/boston/housing.data',
                        sep='\s+',
                        header=None)

boston_df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT',
                     'MEDV']

boston_df['int_RM'] = boston_df['RM'].astype(int)

sns.violinplot('int_RM', 'MEDV', data=boston_df, hue='CHAS', split=True, palette='seismic')
plt.savefig('plots/12-seaborn_categorical_2/boston_int_RM_MEDV_CHAS_violinplot.png')
plt.clf()

sns.swarmplot('int_RM', 'MEDV', data=boston_df, hue='CHAS', split=True)
plt.savefig('plots/12-seaborn_categorical_2/boston_int_RM_MEDV_CHAS_swarmplot.png')

plt.close()
