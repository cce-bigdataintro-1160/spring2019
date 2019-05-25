#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

linear = np.arange(1, 20)
square = linear ** 2
log = np.log(linear)
random = np.random.randint(0, 100, 20)

plt.plot(linear)
plt.plot(square)
plt.plot(log)
plt.plot(random)

# X, y
# plt.plot(log, square)

plt.title('Linear Plot')
plt.xlabel('Index')
plt.ylabel('Linear Y')

plt.show()

plt.close()
