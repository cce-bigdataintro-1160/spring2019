import pandas as pd

pd.options.mode.chained_assignment = None

spotify = pd.read_csv('data/top2018.csv')
print(spotify.head(5).to_string())

# Replacing a given arbitrary value value with another arbitrary value
spotify.replace('Drake', 'DRAKE (UPPER CASED)', inplace=True)
# spotify['artists'].replace('Drake', 'DRAKE (UPPER CASED)', inplace=True)

print(spotify.head(5).to_string())
