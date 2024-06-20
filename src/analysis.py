import numpy as np
import pandas as pd
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import os
# New function adding features

def analyze_data(df):
    output_dir = 'plot_output'
    os.makedirs(output_dir, exist_ok=True)
    print(df.describe())

    # Adding Total Energy Consumption, Natural Gas Energy Consumption, and Electrical/Natural Gas Ratio column
    NATURAL_GAS_ENERGY_DENSITY = 0.303634232 # million kWh per 1 MMcf, from EIA conversion calculator. assuming natural gas is in standard volume
    df['Natural Gas Energy Consumption (million kWh)'] = df['Natural Gas Consumption (MMcf)']*NATURAL_GAS_ENERGY_DENSITY 
    df['Total Energy Consumption (million kWh)'] = df['Natural Gas Energy Consumption (million kWh)']+df['Electrical Consumption (million kWh)']
    df['Electrical/Natural Gas Consumption Ratio'] = df['Electrical Consumption (million kWh)'] / df['Natural Gas Energy Consumption (million kWh)']
    print(df)

    # ******
    new_df = df.pivot_table("Natural Gas Consumption (MMcf)", index=["Month"], columns=["Year"])

    df["DateTime"] = df.index.get_level_values('Year').astype(str) + '-' + df.index.get_level_values('Month').astype(str)
    df["DateTime"] = pd.to_datetime(df["DateTime"], format="%Y-%m")

    total_energy_df = df.pivot_table("Total Energy Consumption (million kWh)", index=["DateTime"])
    elec_consumption_df = df.pivot_table('Electrical Consumption (million kWh)', index = ['DateTime'])
    natural_gas_energy_df = df.pivot_table('Natural Gas Energy Consumption (million kWh)', index = ['DateTime'])
    dd_df = df.pivot_table('DD', index = ['DateTime'])
    df_year = df.pivot_table("Total Energy Consumption (million kWh)", index = 'Month', columns = 'Year')

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

    # # Pivot table, grouped by datetime
    # grouped_datetime_df = df.pivot_table(index = 'DateTime', aggfunc={'Total Energy Consumption (million kWh)':'mean', 'DD':'mean'})

    # # Consumption vs Degree Days

    # plt.scatter(x=grouped_datetime_df['DD'], y=grouped_datetime_df['Total Energy Consumption (million kWh)'], s = 2)
    # plt.title('Monthly Energy Consumption vs. Degree Days')
    # plt.xlabel('Degree Days')
    # plt.ylabel('Energy Consumption (million kWh)')
    # plt.tight_layout()
    # plt.savefig(os.path.join(output_dir, 'consumption_vs_ddays.png'))
    # plt.close()

    # # Energy Consumption Over Time
    # plt.figure()
    # plt.plot(total_energy_df)
    # plt.xlabel('Date')
    # plt.ylabel('Energy Consumption (million kWh)')

    # elec_consumption = plt.subplot()
    # elec_consumption.plot(elec_consumption_df)

    # ng_energy_consumption = plt.subplot()
    # ng_energy_consumption.plot(natural_gas_energy_df)

    # plt.legend(['Monthly Total Energy Consumption (million kWh)', 'Monthly Electrical Consumption (million kWh)', 'Monthly Natural Gas Energy Consumption (million kWh)'])
    # plt.tight_layout()
    # plt.savefig(os.path.join(output_dir, 'energy_consumption_over_time.png'))
    # plt.close()

    # # Degree Days Over Time
    # plt.plot(dd_df)
    # plt.title('Degree Days Over Time')
    # plt.xlabel('Date')
    # plt.ylabel('Degree Days')
    # plt.tight_layout()
    # plt.savefig(os.path.join(output_dir, 'degree_days_over_time.png'))
    # plt.close()

    # Average Monthly Consumption by Season
    print('\n' * 2)
    print('******** Average Monthly Consumption and Degree Days by Season ********')
    winter_averages = grouped_months_df.loc[[12, 1, 2]].mean()
    spring_averages = grouped_months_df.loc[[3, 4, 5]].mean()
    summer_averages = grouped_months_df.loc[[6, 7, 8]].mean()
    fall_averages = grouped_months_df.loc[[9, 10, 11]].mean()
    seasonal_averages = pd.DataFrame({'Winter': winter_averages, 'Spring': spring_averages, 'Summer': summer_averages, 'Fall': fall_averages}).transpose()
    print(seasonal_averages)
    return df
