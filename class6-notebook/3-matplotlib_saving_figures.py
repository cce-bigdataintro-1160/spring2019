#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import os


linear = np.arange(1, 20)
square = linear ** 2
log = np.log(linear)
random = np.random.randint(0, 100, 20)

fig, axes = plt.subplots(3, 1, figsize=(5,5))

axes[0].plot(linear)
axes[1].plot(square)
axes[2].plot(log)

os.makedirs('plots/3-matplotlib_saving_figures', exist_ok=True)

plt.savefig('plots/3-matplotlib_saving_figures/plot.png', dpi=300)

plt.close()
