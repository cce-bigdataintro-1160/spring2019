#!/usr/bin/env python3

import pandas as pd


def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')

# Creating Dataframe from Files
titanic = pd.read_csv(filepath_or_buffer='data/titanic/train.csv',
                      sep=',',
                      header=0)

# Getting DataFrames information
pretty_print("titanic dataframe", titanic.to_string())
pretty_print("titanic columns", titanic.columns)

# Selecting DataFrame Columns
pretty_print("checking the type of the Name column", type(titanic['Name']))
pretty_print("selecting the Name column", titanic['Name'])
pretty_print("selecting the Name, Fare and Age columns", titanic[['Name', 'Fare', 'Age']])
pretty_print("suming up the Fare and Age columns", titanic['Fare'] + titanic['Age'])

# Selecting DataFrame Rows and Columns by name with loc function
pretty_print("selecting the row 1", titanic.loc[1])
pretty_print("selecting rows 1, 2 and 3, and also the columns Name and Sex", titanic.loc[[1, 2, 3], ['Name', 'Sex']])
pretty_print("selecting ranges of rows and columns", titanic.loc[37:43, 'Name':'Cabin'])

# Selecting DataFrame Rows and Columns by index with iloc function
pretty_print("selecting the row 1 by index", titanic.iloc[1])
pretty_print("selecting rows 1, 2 and 3, and also the columns Name and Sex by index", titanic.iloc[[1, 2, 3], [3, 4]])
pretty_print("selecting ranges of rows and columns by index", titanic.iloc[37:49, 3:5])

# Selecting DataFrame Rows by a condition
pretty_print("selecting rows by criteria", titanic[titanic['Age'] > 30])
pretty_print("selecting rows by multiple criteria",
             titanic[(titanic['Age'] > 30) & (titanic['Fare'] > 30) & (titanic['Survived'] == 1)])

# Extracting DataFrame correlations
pretty_print("correlation matrix", titanic.corr().to_string())