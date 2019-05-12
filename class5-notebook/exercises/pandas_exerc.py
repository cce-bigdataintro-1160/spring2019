#!/usr/bin/env python3

import numpy as np
import pandas as pd

insurance_df = pd.read_csv(filepath_or_buffer='../data/insurance.csv',
                           sep=',',
                           header=0)
# 1
print(insurance_df.to_string())
print(len(insurance_df))
print(insurance_df.head(n=1))
print(insurance_df.columns)
print(insurance_df.index)
print(insurance_df.dtypes)
print(insurance_df.shape)
print(insurance_df.info())
print(insurance_df.describe())

# 2
print(insurance_df['age'])

# 3
print(insurance_df[['age', 'children', 'charges']])

# 4
print(insurance_df[['age', 'children', 'charges']].head(5))

# 5
print(insurance_df.describe())

# 6
print(insurance_df[insurance_df['charges'] == 10797.3362])

# 7
print(insurance_df[insurance_df['charges'] == insurance_df['charges'].max()])

# 8
print(insurance_df['region'].value_counts())

# 9
print(insurance_df['children'].value_counts())

# 10 and 11
print(insurance_df.corr())
