import matplotlib.pyplot as plt
import pandas as pd
import os
from datetime import datetime


def plot_energy_consumption(df, plot_type='line'):
    '''
    Plots the Total Energy Consumption, Natural Gas Consumption, 
    and Electrical Consumption over time.

    Parameters:
    df (DataFrame): The dataframe to plot.
    plot_type (str): The type of plot to create ('line' or 'scatter').
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
        region_data['Date'] = pd.to_datetime(region_data.assign(day=1)[['Year', 'Month', 'day']])
        if plot_type == 'line':
            plt.plot(region_data['Date'], region_data['Natural Gas Consumption (MMcf)'], label=region, alpha=0.7)
        elif plot_type == 'scatter':
            plt.scatter(region_data['Date'], region_data['Natural Gas Consumption (MMcf)'], label=region, alpha=0.7)

    plt.title('Natural Gas Consumption Over Time by Region')
    plt.xlabel('Date')
    plt.ylabel('Natural Gas Consumption (MMcf)')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'natural_gas_consumption.png'))
    plt.close()

    # Plot Electrical Consumption
    plt.figure(figsize=(12, 6))
    for region in df['Region'].unique():
        region_data = df[df['Region'] == region]
        region_data['Date'] = pd.to_datetime(region_data.assign(day=1)[['Year', 'Month', 'day']])
        if plot_type == 'line':
            plt.plot(region_data['Date'], region_data['Electrical Consumption (million kWh)'], label=region, alpha=0.7)
        elif plot_type == 'scatter':
            plt.scatter(region_data['Date'], region_data['Electrical Consumption (million kWh)'], label=region, alpha=0.7)

    plt.title('Electrical Consumption Over Time by Region')
    plt.xlabel('Date')
    plt.ylabel('Electrical Consumption (million kWh)')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'electrical_consumption.png'))
    plt.close()

    # Plot Total Energy Consumption
    plt.figure(figsize=(12, 6))
    for region in df['Region'].unique():
        region_data = df[df['Region'] == region]
        region_data['Date'] = pd.to_datetime(region_data.assign(day=1)[['Year', 'Month', 'day']])
        if plot_type == 'line':
            plt.plot(region_data['Date'], region_data['Total Energy Consumption (million kWh)'], label=region, alpha=0.7)
        elif plot_type == 'scatter':
            plt.scatter(region_data['Date'], region_data['Total Energy Consumption (million kWh)'], label=region, alpha=0.7)

    plt.title('Total Energy Consumption Over Time by Region')
    plt.xlabel('Date')
    plt.ylabel('Total Energy Consumption (million kWh)')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'total_energy_consumption.png'))
    plt.close()

    # Plot Absolute Degree Days (DD)
    plt.figure(figsize=(12, 6))
    for region in df['Region'].unique():
        region_data = df[df['Region'] == region]
        region_data['Date'] = pd.to_datetime(region_data.assign(day=1)[['Year', 'Month', 'day']])
        region_data['absolute_DD'] = region_data['DD'].abs()
        if plot_type == 'line':
            plt.plot(region_data['Date'], region_data['absolute_DD'], label=region, alpha=0.7)
        elif plot_type == 'scatter':
            plt.scatter(region_data['Date'], region_data['absolute_DD'], label=region, alpha=0.7)

    plt.title('Absolute Degree Days (DD) Over Time by Region')
    plt.xlabel('Date')
    plt.ylabel('Absolute Degree Days (DD)')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'absolute_degree_days.png'))
    plt.close()
