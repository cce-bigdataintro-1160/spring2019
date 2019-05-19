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

os.makedirs('plots/8-matplotlib_dataset_multifeature', exist_ok=True)

fig, axes = plt.subplots(1, 1, figsize=(5, 5))
axes.scatter(df['alcohol'], df['total_phenols'], label=f'alcohol to total_phenols', color='green', marker='x')
axes.scatter(df['alcohol'], df['color_intensity'], label=f'alcohol to color_intensity', color='red', marker='o')
axes.scatter(df['alcohol'], df['class'], label=f'alcohol to class', color='blue', marker='v')
axes.set_title(f'Alcohol comparisons')
axes.legend()
plt.savefig(
    f'plots/8-matplotlib_dataset_multifeature/alcohol_total_phenols_color_intensity_class.png',
    dpi=300)

plt.close()

# multie featuer with color and size
# *2D or 3D* with at least *4* features at a time: add multiple plots on same visualization,
# like https://github.com/zzzhengzzz/Class7hwk/blob/master/run.py loopable too
# https://github.com/bmshahrier/class7-hwk/blob/master/data_expo.py
# https://github.com/zangdongxiao/class7hwk/blob/master/mypython.py
