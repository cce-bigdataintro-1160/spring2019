import pandas as pd
import matplotlib.pyplot as plt

insurance = pd.read_csv(filepath_or_buffer='data/insurance.csv',
                      sep=',',
                      header=0)

plt.scatter(insurance['bmi'], insurance['charges'])
plt.title('Fare by Index')
plt.xlabel('Index')
plt.ylabel('Fare')
plt.savefig(f'plots/fare_by_index_plot.png', format='png')
plt.clf()
