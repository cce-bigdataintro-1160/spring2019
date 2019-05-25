#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns

df = pd.read_csv('data/diabetes.data',
                 sep='\\s+',
                 header=0)

os.makedirs('plots/11-seaborn_distplot', exist_ok=True)

sns.set()

sns.distplot(df['BMI'], bins=15, kde=False)
plt.savefig('plots/11-seaborn_distplot/diabetes_bmi_distplot.png')

plt.close()
