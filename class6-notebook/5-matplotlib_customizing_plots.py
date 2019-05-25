#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import os

linear = np.arange(1, 20)
square = linear ** 2
log = np.log(linear)
random = np.random.randint(0, 100, 20)

#Solarize_light2, bmh,grayscale, dark_background, ggplot
plt.style.use("ggplot")

fig, axes = plt.subplots(1, 1, figsize=(5, 5))

axes.plot(log, label='Linear', color='blue', linestyle='--', linewidth=2, alpha=0.8, marker='o')
axes.set_title('Linear Plot')
axes.set_xlabel('Index')
axes.set_ylabel('Linear')
axes.legend()

os.makedirs('plots/5-matplotlib_customizing_plots', exist_ok=True)

plt.savefig('plots/5-matplotlib_customizing_plots/customized_plot.png', dpi=300)

plt.close()
