#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import os

linear = np.arange(1, 20)
square = linear ** 2
log = np.log(linear)
random = np.random.randint(0, 100, 20)

fig, axes = plt.subplots(2, 1, figsize=(5, 5))

axes[0].plot(linear, label='Linear')
axes[0].set_title('Linear Plot')
axes[0].set_xlabel('Index')
axes[0].set_xticklabels(['one_x','two_x','three_x','four_x'])
axes[0].set_yticklabels(['one_y','two_y','three_y','four_y'])
axes[0].legend()

axes[1].plot(square)

plt.tight_layout()

os.makedirs('plots/4-matplotlib_decorating_plots', exist_ok=True)

plt.savefig('plots/4-matplotlib_decorating_plots/decorated_plot.png', dpi=300)

plt.close()
