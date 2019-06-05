import pandas as pd

pd.options.mode.chained_assignment = None

heart = pd.read_csv('data/heart.csv')
# print(heart.info())
# print(heart.head(5).to_string())
# print(heart.describe().to_string())
print(heart.columns)

heart.rename({'cp': 'chest pain type', 'fbs': 'fasting blood sugar'}, axis=1, inplace=True)

print(heart.columns)
