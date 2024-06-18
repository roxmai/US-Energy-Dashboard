import matplotlib.pyplot as plt
import pandas as pd
import os

def plot_energy_consumption(df):
    '''
    Plots the Total Energy Consumption, Natural Gas Consumption, and Electrical Consumption over time.

    Parameters:
    df (DataFrame): The dataframe to plot.
    '''
    
    # Aggregate data at the region level
    columns_to_exclude = ['DateTime']  # Specify columns to exclude from the sum operation
    columns_to_sum = [col for col in df.columns if col not in columns_to_exclude + ['Region', 'Year', 'Month']]  
    df = df.groupby(['Region', 'Year', 'Month'])[columns_to_sum].sum().reset_index()

    # Ensure the output directory exists
    output_dir = 'plot_output'
    os.makedirs(output_dir, exist_ok=True)

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
    plt.savefig(os.path.join(output_dir, 'natural_gas_consumption.png'))
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
    plt.savefig(os.path.join(output_dir, 'electrical_consumption.png'))
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
    plt.savefig(os.path.join(output_dir, 'total_energy_consumption.png'))
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
    plt.savefig(os.path.join(output_dir, 'hdd_over_time.png'))
    plt.close()