import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('../data/boston/housing.data',
                 sep='\s+',
                 header=None)

df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

plt.style.use('ggplot')

#Exercise 4 - add color, marker and alpha
fig, axes = plt.subplots(1, 1, figsize=(5, 5))

axes.scatter(df['MEDV'], df['CRIM'], color='black', marker='s', alpha=0.8)
axes.set_xlabel('MEDV')
axes.set_ylabel('CRIM')
axes.set_title('Value of houses vs Crime')

plt.savefig("scatter_color_marker_alpha.png")
