import numpy as np
import pandas as pd
from src.DataframeBuilder import df

print(df.describe())

# Adding Total Energy Consumption, Natural Gas Energy Consumption, and Electrical/Natural Gas Ratio column
print('\n'*2)
print('******** Natural Gas, Electricity, Total Energy Consumption, Degree Days By State By Month,Year ********')
natural_gas_energy_density = 0.303634232 # million kWh per 1 MMcf, from EIA conversion calculator. assuming natural gas is in standard volume
df['Natural Gas Energy Consumption (million kWh)'] = df['Natural Gas Consumption (MMcf)']*natural_gas_energy_density 
df['Total Energy Consumption (million kWh)'] = df['Natural Gas Energy Consumption (million kWh)']+df['Electrical Consumption (million kWh)']
df['Electrical/Natural Gas Consumption Ratio'] = df['Electrical Consumption (million kWh)']/df['Natural Gas Energy Consumption (million kWh)']
print(df.head(5))

# Total Consumption Over all years
print('\n'*2)
print('******** Total Consumption in U.S. over all years ********')
total_natural_gas = np.sum(df['Natural Gas Energy Consumption (million kWh)'])
print('Total Natural Gas Energy Consumption:',total_natural_gas, 'million kWh')
total_electricity = np.sum(df['Electrical Consumption (million kWh)'])
print('Total Electricity Consumption:',total_electricity, 'million kWh')
total_energy = np.sum(df['Total Energy Consumption (million kWh)'])
print('Total Energy Consumption:',total_energy, 'million kWh')

# Average Monthly Consumption by Month
print('\n'*2)
print('******** Average Monthly Consumption and Degree Days by Month ********')
grouped_months_natural_gas_df = df.groupby('Month')['Natural Gas Consumption (MMcf)'].mean()
grouped_months_electricity_df = df.groupby('Month')['Electrical Consumption (million kWh)'].mean()
grouped_months_total_energy_df = df.groupby('Month')['Total Energy Consumption (million kWh)'].mean()
grouped_months_degree_days_df = df.groupby('Month')['DD'].mean()
grouped_months_df = pd.DataFrame({'Natural Gas Consumption (MMcf)':grouped_months_natural_gas_df, 'Electrical Consumption (million kWh)':grouped_months_electricity_df, 'Total Energy Consumption (million kWh)': grouped_months_total_energy_df, 'Degree Days': grouped_months_degree_days_df})
print(grouped_months_df)

# Average Monthly Consumption by Season
print('\n'*2)
print('******** Average Monthly Consumption and Degree Days by Season ********')
winter_averages = grouped_months_df.loc[[12,1,2]].mean()
spring_averages = grouped_months_df.loc[[3,4,5]].mean()
summer_averages = grouped_months_df.loc[[6,7,8]].mean()
fall_averages = grouped_months_df.loc[[9,10,11]].mean()
seasonal_averages = pd.DataFrame({'Winter': winter_averages, 'Spring':spring_averages, 'Summer': summer_averages, 'Fall': fall_averages}).transpose()
print(seasonal_averages)
