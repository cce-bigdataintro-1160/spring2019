#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns
import numpy as np

df = pd.read_csv('data/wine.data',
                 sep=',',
                 header=0)

df.columns = ['class', 'alcohol', 'malic_acid', 'ash', 'alcalinity_of_ash', 'magnesium', 'total_phenols', 'flavanoids',
              'nonflavanoid_phenols', 'proanthocyanins', 'color_intensity', 'hue', 'od280 od315_of_diluted_wines',
              'proline']

os.makedirs('plots/13-seaborn_heatmap', exist_ok=True)

sns.set()

fig, ax = plt.subplots(figsize=(12,12))
sns.heatmap(df.corr(), annot=True, cmap='autumn')
ax.set_xticklabels(df.columns, rotation=45)
ax.set_yticklabels(df.columns, rotation=45)
plt.savefig('plots/13-seaborn_heatmap/wine_heatmap.png')

plt.close()
