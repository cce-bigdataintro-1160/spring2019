import pandas as pd
pd.options.mode.chained_assignment = None

spotify = pd.read_csv('data/top2018.csv')
print(len(spotify))
# print(spotify.info())
# print(spotify.head(5).to_string())
# print(spotify.describe().to_string())

# Splitting the original dataframe in two
df1 = spotify.iloc[:50, :]
df2 = spotify.iloc[50:, :]

print(len(df1))
print(len(df2))

# Concatenating it back into one
concatenated_df = pd.concat([df1, df2], sort=False)
print(len(concatenated_df))


