import pandas as pd

pd.options.mode.chained_assignment = None

spotify = pd.read_csv('data/top2018.csv')
print(spotify.head(5).to_string())

# Updating the values of an existing column to upper case
spotify['artists'] = spotify['artists'].apply(lambda x: x.upper())

# Adding a new column with the length of the name of each artist
# spotify['artists_length'] = spotify['artists'].apply(lambda x: len(x))

# Passing a function that identify songs that contain the word 'love' on the name
# def has_love(x):
#     if 'love' in x.lower():
#         return 1
#     else:
#         return 0
#
# spotify['name_has_love'] = spotify['name'].apply(has_love)

print(spotify.head(5).to_string())
