#!/usr/bin/env python

import pandas as pd
import numpy as np
from argparse import ArgumentParser


# Receive csvfile, headers and separator arguments
parser = ArgumentParser(description='A CSV reader + stats maker')
parser.add_argument('csvfile', type=str, help='Path to the input csv file.')
parser.add_argument('headers', type=str, help='Path to the headers csv file.')
parser.add_argument('separator', type=str, help='Separator for data file')
parsed_args = parser.parse_args()

file_path = parsed_args.csvfile
separator = parsed_args.separator
headers_path = parsed_args.headers

# Read both the data and headers file
df = pd.read_csv(file_path, sep=separator) #\s+|,
df.columns = pd.read_csv(headers_path).columns

print('Regular')
print(df.shape)
print(df.head(3))

transposed_df = df.transpose()

print('Transposed')
print(transposed_df.shape)
print(transposed_df.head(3))

print('Mean')
print(np.mean(df))
print('Standard Deviation')
print(np.std(df))
