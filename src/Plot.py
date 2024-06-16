import matplotlib.pyplot as plt
import pandas as pd

def plot_energy_consumption(df):
    '''
    Plots the Total Energy Consumption, Natural Gas Consumption, and Electrical Consumption over time.

    Parameters:
    df (DataFrame): The dataframe to plot.
    '''
    df = df.reset_index()

    # Plot Natural Gas Consumption
    plt.figure(figsize=(12, 6))
    for region in df['Region'].unique():
        region_data = df[df['Region'] == region]
        plt.plot(region_data['Year'] + region_data['Month']/12, 
                    region_data['Natural Gas Consumption (MMcf)'], label=region, alpha=0.7)

    plt.title('Natural Gas Consumption Over Time by Region')
    plt.xlabel('Year')
    plt.ylabel('Natural Gas Consumption (MMcf)')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig('natural_gas_consumption.png')
    plt.close()

    # Plot Electrical Consumption
    plt.figure(figsize=(12, 6))
    for region in df['Region'].unique():
        region_data = df[df['Region'] == region]
        plt.plot(region_data['Year'] + region_data['Month']/12, 
                 region_data['Electrical Consumption (million kWh)'], label=region, alpha=0.7)

    plt.title('Electrical Consumption Over Time by Region')
    plt.xlabel('Year')
    plt.ylabel('Electrical Consumption (million kWh)')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig('electrical_consumption.png')
    plt.close()

    # Plot Total Energy Consumption
    plt.figure(figsize=(12, 6))
    for region in df['Region'].unique():
        region_data = df[df['Region'] == region]
        plt.plot(region_data['Year'] + region_data['Month']/12, 
                 region_data['Total Energy Consumption (million kWh)'], label=region, alpha=0.7)

    plt.title('Total Energy Consumption Over Time by Region')
    plt.xlabel('Year')
    plt.ylabel('Total Energy Consumption (million kWh)')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig('total_energy_consumption.png')
    plt.close()

    # Plot Heating Degree Days (HDD)
    plt.figure(figsize=(12, 6))
    for region in df['Region'].unique():
        region_data = df[df['Region'] == region]
        plt.plot(region_data['Year'] + region_data['Month']/12, 
                    region_data['HDD'], label=region, alpha=0.7)

    plt.title('Heating Degree Days (HDD) Over Time by Region')
    plt.xlabel('Year')
    plt.ylabel('HDD')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig('hdd_over_time.png')
    plt.close()