from src.DataframeBuilder import build_data_frame
from src.Analysis import analyze_data
from src.Plot import plot_energy_consumption # Importing the plot function
import numpy as np
import pandas as pd


def main():
    # build the dataframe using the provided function
    df = build_data_frame()

    # Analyze data
    df = analyze_data(df)  # Calling the function before getting analytics

    # General Data Analysis has been done. Now moving to specific analysis.
    print('\nGeneral Statistics and Analysis Done.\n')

    # Ask user for region input
    print("Data available regions: East North Central, East South Central, Middle Atlantic, Mountain, New England, Pacific, South Atlantic, West North Central, West South Central")
    region_input = input("Enter region you want to analyze? (e.g., 'New England'): ").strip()

    # Filter the dataframe by the selected region
    available_regions = df.index.get_level_values('Region').unique()
    if region_input in available_regions:
        df = df[df.index.get_level_values('Region') == region_input]
    else:
        print("Invalid region. Please restart the program and select a valid region.")
        return

    time_frame = input("Would you like to analyze 'yearly' or 'monthly': ").strip().lower()

    if time_frame == 'yearly':
        year = int(input("Enter the year you want to analyze from 2001 to 2024 (e.g. 2003): "))
        df_year = df[df.index.get_level_values('Year') == year]
        if df_year.empty:
            print('No data available for the selected year. Please restart the program and select a valid year.')
            return

        # Total consumption statistics
        total_power_consumption = df_year['Electrical Consumption (million kWh)'].sum()
        total_natural_gas_consumption = df_year['Natural Gas Energy Consumption (million kWh)'].sum()
        total_energy_consumption = df_year['Total Energy Consumption (million kWh)'].sum()

        print(f"\nFor the region {region_input} in the year {year}:")
        print(f"Total power consumption: {total_power_consumption:.2f} million kWh")
        print(f"Total natural gas energy consumption: {total_natural_gas_consumption:.2f} million kWh")
        print(f"Total energy consumption: {total_energy_consumption:.2f} million kWh")

        # Average monthly energy consumption
        average_monthly_power = df_year['Electrical Consumption (million kWh)'].mean()
        average_monthly_natural_gas = df_year['Natural Gas Energy Consumption (million kWh)'].mean()
        average_monthly_energy = df_year['Total Energy Consumption (million kWh)'].mean()

        print(f"Average monthly power consumption: {average_monthly_power:.2f} million kWh")
        print(f"Average monthly natural gas consumption: {average_monthly_natural_gas:.2f} million kWh")
        print(f"Average monthly energy consumption: {average_monthly_energy:.2f} million kWh")

        # Plot energy consumption vs degree days
        plot_energy_consumption(df_year)

    elif time_frame == 'monthly':
        year_start = int(input("Enter the start year you want to analyze from 2001 to 2024 (e.g. 2003): "))
        year_end = int(input("Enter the end year you want to analyze from 2001 to 2024 (e.g. 2003): "))
        df_years = df[(df.index.get_level_values('Year') >= year_start) & (df.index.get_level_values('Year') <= year_end)]
        if df_years.empty:
            print('No data available for the selected years. Please restart the program and select a valid range.')
            return

        season_or_month = input("Would you like to analyze by 'month' or 'season': ").strip().lower()

        if season_or_month == 'month':
            month = int(input('Enter the month (1-12) you want to analyze: '))
            df_month = df_years[df_years.index.get_level_values('Month') == month]
            if df_month.empty:
                print('No data available for the selected month. Please restart the program and select a valid month.')
                return

            # Average monthly consumption statistics
            average_power = df_month['Electrical Consumption (million kWh)'].mean()
            average_natural_gas = df_month['Natural Gas Energy Consumption (million kWh)'].mean()
            average_energy = df_month['Total Energy Consumption (million kWh)'].mean()

            print(f"\nFor the region {region_input} from year {year_start} to {year_end}, month {month}:")
            print(f"Average monthly power consumption: {average_power:.2f} million kWh")
            print(f"Average monthly natural gas consumption: {average_natural_gas:.2f} million kWh")
            print(f"Average monthly energy consumption: {average_energy:.2f} million kWh")

            # Plot energy consumption vs degree days (Scatter Plot for 'monthly')
            plot_energy_consumption(df_month, plot_type='scatter')

        elif season_or_month == 'season':
            season = input("Enter the season (Winter, Spring, Summer, Autumn) you want to analyze: ").strip().capitalize()
            month_map = {'Winter': [12, 1, 2], 'Spring': [3, 4, 5], 'Summer': [6, 7, 8], 'Autumn': [9, 10, 11]}

            if season not in month_map.keys():
                print('Invalid season. Please restart the program and enter a valid season.')
                return

            df_season = df_years[df_years.index.get_level_values('Month').isin(month_map[season])]
            if df_season.empty:
                print('No data available for the selected season. Please restart the program and select a valid season.')
                return

            # Average seasonal consumption statistics
            average_power = df_season['Electrical Consumption (million kWh)'].mean()
            average_natural_gas = df_season['Natural Gas Energy Consumption (million kWh)'].mean()
            average_energy = df_season['Total Energy Consumption (million kWh)'].mean()

            print(f"\nFor the region {region_input} from year {year_start} to {year_end}, season {season}:")
            print(f"Average seasonal power consumption: {average_power:.2f} million kWh")
            print(f"Average seasonal natural gas consumption: {average_natural_gas:.2f} million kWh")
            print(f"Average seasonal energy consumption: {average_energy:.2f} million kWh")

            # Plot energy consumption vs degree days
            plot_energy_consumption(df_season)
        else:
            print('Invalid input. Please restart the program and enter either "month" or "season".')
            return

    else:
        print('Invalid input. Please restart the program and enter either "yearly" or "monthly".')
        return


if __name__ == '__main__':
    main()