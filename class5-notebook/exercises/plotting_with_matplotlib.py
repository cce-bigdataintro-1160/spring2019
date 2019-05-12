import pandas as pd
import os
import matplotlib.pyplot as plt

# Creating Dataframe from Files
insurance_df = pd.read_csv(filepath_or_buffer='../data/insurance.csv',
                      sep=',',
                      header=0)

os.makedirs('plots', exist_ok=True)

#Plotting line chart
plt.plot(insurance_df['children'], color='green')
plt.title('children by Index')
plt.xlabel('Index')
plt.ylabel('children')
plt.savefig(f'plots/charges_by_index_plot.png', format='png')
plt.clf()

# Plotting histogram
plt.hist(insurance_df['charges'], bins=10, color='g')
plt.title('charges')
plt.xlabel('charges')
plt.ylabel('Count')
plt.savefig(f'plots/bmi_hist.png', format='png')
plt.clf()

#Plotting scatterplot
plt.scatter(insurance_df['bmi'], insurance_df['charges'], color='b')
plt.title('bmi to charges')
plt.xlabel('bmi')
plt.ylabel('charges')
plt.savefig(f'plots/age_to_fare.png', format='png')