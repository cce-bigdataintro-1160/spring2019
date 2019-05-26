import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('../data/boston/housing.data',
                 sep='\s+',
                 header=None)

df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

plt.style.use('ggplot')

fig, axes = plt.subplots(1, 1, figsize=(5, 5))

# Exercise 6 - Multifeature plot
axes.scatter(df['MEDV'], df['CRIM'], marker='^', label='CRIME')
axes.scatter(df['MEDV'], df['AGE']*0.5, marker='s', label='AGE')
axes.scatter(df['MEDV'], df['PTRATIO'], marker='v', label='PTRATIO')
axes.set_xlabel('MEDV')
axes.set_title('Value of Houses vs Crime')
plt.legend()

plt.savefig("multiple_plots_size.png")
