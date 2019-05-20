#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import os

linear = np.arange(1, 20)
square = linear ** 2
log = np.log(linear)
random = np.random.randint(0, 100, 20)

fig, axes = plt.subplots(2, 3, figsize=(10, 5))

axes[0][0].plot(linear)
axes[0][1].plot(square)
axes[0][2].plot(log)
axes[1][0].plot(random)
axes[1][1].plot(log)
axes[1][2].plot(random)

plt.tight_layout()

os.makedirs('plots/3-matplotlib_saving_multiple_plot_figure', exist_ok=True)

plt.savefig('plots/3-matplotlib_saving_multiple_plot_figure/plot.png', dpi=300)

plt.close()
