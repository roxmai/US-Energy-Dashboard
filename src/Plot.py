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

    print(plt)
    # Plot Rlectrical Consumption

    # Plot Total Energy Consumption

    # Plot Hheating Degree Days (HDD)