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

plt.figure()
sns.distplot(df['BMI'], bins=15, kde=False)
plt.savefig('plots/11-seaborn_distplot/bmi_distplot.png')

plt.figure()
sns.distplot(df['S3'], bins=50, kde=False)
plt.savefig('plots/11-seaborn_distplot/s3_distplot.png')

plt.figure()
sns.distplot(df['AGE'], bins=30, kde=False)
plt.savefig('plots/11-seaborn_distplot/age_distplot.png')

plt.close()
