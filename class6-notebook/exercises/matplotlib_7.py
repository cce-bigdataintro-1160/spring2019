import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('../data/boston/housing.data',
                 sep='\s+',
                 header=None)

df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

plt.style.use('ggplot')

fig, axes = plt.subplots(1, 1, figsize=(5, 5))

# Exercise 7 - Multifeature plot with color and size
axes.scatter(df['MEDV'], df['CRIM'], color='black', marker='^', alpha=0.8, s=df['INDUS']*2, label='CRIME')
axes.scatter(df['MEDV'], df['AGE']*0.5, color='red', marker='s', alpha=0.8, s=df['INDUS']*2, label='AGE')
axes.scatter(df['MEDV'], df['PTRATIO'], color='purple', marker='o', alpha=0.8, s=df['INDUS']*2, label='PTRATIO')
axes.set_xlabel('MEDV')
axes.set_title('Value of houses vs Crime and Size by Industry')
plt.legend()

plt.savefig("multiple_plots_size_and_color.png")
