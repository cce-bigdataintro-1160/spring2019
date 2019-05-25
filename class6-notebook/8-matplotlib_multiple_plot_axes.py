#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

df = pd.read_csv('data/wine.data',
                 sep=',',
                 header=0)

df.columns = ['class', 'alcohol', 'malic_acid', 'ash', 'alcalinity_of_ash', 'magnesium', 'total_phenols', 'flavanoids',
              'nonflavanoid_phenols', 'proanthocyanins', 'color_intensity', 'hue', 'od280 od315_of_diluted_wines',
              'proline']

os.makedirs('plots/8-matplotlib_multiple_plot_axes', exist_ok=True)

plt.style.use("ggplot")

fig, axes = plt.subplots(1, 1, figsize=(5, 5))
axes.grid(axis='y', alpha=0.5)
axes.scatter(df['alcohol'], df['total_phenols'])
axes.scatter(df['alcohol'], df['color_intensity'])
axes.scatter(df['alcohol'], df['class'])
axes.set_title(f'Alcohol comparisons')
axes.legend()
plt.savefig(f'plots/8-matplotlib_multiple_plot_axes/wine_alcohol_total_phenols_color_intensity_class_scatter.png', dpi=300)



plt.close()








# Multifeature with size
# fig, axes = plt.subplots(1, 1, figsize=(5, 5))
# axes.grid(axis='y', alpha=0.5)
# axes.scatter(df['alcohol'], df['total_phenols'], s=(df['alcohol'] * df['total_phenols']) * 2,
#              label=f'alcohol to total_phenols', color='green', marker='x', edgecolors='w', alpha=0.7)
# axes.scatter(df['alcohol'], df['color_intensity'], s=(df['alcohol'] * df['color_intensity']) * 2,
#              label=f'alcohol to color_intensity', color='orange', marker='s', edgecolors='w', alpha=0.7)
# axes.scatter(df['alcohol'], df['class'], s=(df['alcohol'] * df['class']) * 2, label=f'alcohol to class', color='purple',
#              marker='^', edgecolors='w', alpha=0.7)
# axes.set_title(f'Alcohol comparisons')
# axes.legend()
# plt.savefig(f'plots/8-matplotlib_multiple_plot_axes/wine_alcohol_total_phenols_color_intensity_class_customized_scatter.png', dpi=300)