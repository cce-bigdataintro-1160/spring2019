#!/usr/bin/env python3

import numpy as np
import pandas as pd


def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')


orders = pd.Series(data=[300.50, 60, 123.40, 60, np.nan],
                   index=['Customer 1', 'Customer 2', 'Customer 3', 'Customer 4', 'Customer 5'])

pretty_print("orders", orders.to_string())
pretty_print("first row of orders", orders.head(n=1))
pretty_print("orders indexes", orders.index)
pretty_print("order types", orders.dtypes)
pretty_print("orders shape", orders.shape)

pretty_print("orders description with types", orders.describe())
pretty_print("orders sorted values", orders.sort_values())
pretty_print("orders counts of values", orders.value_counts())
pretty_print("orders check for null elements", orders.isnull())
