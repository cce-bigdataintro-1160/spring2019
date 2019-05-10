#!/usr/bin/env python3

import pandas as pd


def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')


# Creating Dataframe from Lists
orders = pd.DataFrame(data=[['XB4Z34', 11, 25.50],
                            ['SZA1123', 34, 60],
                            ['P4FF2S', 2, 123.40],
                            ['PL34DS', 10, 1254.23],
                            ['PL34DS', 4, 12.4]],
                      # index=['Customer 1', 'Customer 2', 'Customer 3', 'Customer 4', 'Customer 5'],
                      columns=['Product', 'Qty', 'Price'])

orders.columns = ['Product', 'Qty', 'Price']

# Getting DataFrames information
pretty_print("orders", orders.to_string())
pretty_print("length of orders", len(orders))
pretty_print("first row of orders", orders.head(n=1))
pretty_print("orders columns", orders.columns)
pretty_print("orders indexes", orders.index)
pretty_print("order types", orders.dtypes)
pretty_print("orders shape", orders.shape)
pretty_print("orders summarized information", orders.info())
pretty_print("orders description with types", orders.describe())

# Extracting values from the DataFrames
pretty_print("orders sorted values by price", orders.sort_values(by='Price'))
pretty_print("orders counts of values for Qty", orders['Qty'].value_counts())
pretty_print("orders check for null elements", orders.isnull())
pretty_print("number of unique value counts", orders.nunique())
pretty_print("number of unique Products counts", orders['Product'].unique())
