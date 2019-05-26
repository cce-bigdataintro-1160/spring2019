import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('../data/boston/housing.data',
                 sep='\s+',
                 header=None)

df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

plt.style.use('ggplot')

fig, axes = plt.subplots(2, 1, figsize=(5, 5))

#Exercise 1 - Plot multiple plots and Exercise 2 - Add title and x,y labels
axes[0].plot(df['MEDV'])
axes[0].set_xlabel('Index')
axes[0].set_ylabel('MEDV')
axes[0].set_title('Value of houses')

axes[1].scatter(df['MEDV'], df['CRIM'])
axes[1].set_xlabel('MEDV')
axes[1].set_ylabel('CRIM')
axes[1].set_title('Value of houses vs Crime')

plt.tight_layout()

#Exercise 3 - Save figures
plt.savefig("plot_and_scatter.png")
