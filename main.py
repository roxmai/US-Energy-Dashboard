from src.DataframeBuilder import build_data_frame
from src.analysis import analyze_data
from src.Plot import plot_energy_consumption
import numpy as np
import pandas as pd

def main():
    # build the dataframe using the provided function
    df = build_data_frame()

    # Ask user for region input
    region_input = input("Enter region you want to analyze? (e.g., 'New England', 'Middle Atlantic', etc.): ").strip()

    # Filter the dataframe by the selected region
    available_regions = df.index.get_level_values('Region').unique()
    if region_input in available_regions:
        df = df[df.index.get_level_values('Region') == region_input]
    else:
        print("Invalid region. Please restart the program and select a valid region.")
        return

    # Ask user for year input
    year_input = input("Do you want to analyze a specific year or a range (e.g. 'specific', 'range'): ")

    if year_input == 'specific':
        year = int(input("Enter the year you want to analyze from 2001 to 2021 (e.g. '2003'): "))
        df = df[df.index.get_level_values('Year') == year]
    elif year_input == 'range':
        start_year = int(input('Enter the start year of the range: '))
        end_year = int(input('Enter the end year of the range: '))
        df = df[(df.index.get_level_values('Year') >= start_year) & (df.index.get_level_values('Year') <= end_year)]
    else:
        print('Invalid input. Please restart the program and enter either "specific" or "range".')
        return
    
    # Ask user for the month input
    analysis_type = input("Would you like to analyze the entire duration, a specific month, or a season? Enter 'duration', 'month', or 'season': ").strip().lower()

    if analysis_type == 'month':
        month = int(input('Enter the month (1-12) you want to analyze: '))
        df = df[df.index.get_level_values('Month') == month]
    elif analysis_type == 'season':
        season = int(input("Enter the season you want to analyze (Winter = 1, Spring = 2, Summer = 3, Autumn = 4): "))
        if season == 1:
            df = df[df.index.get_level_values('Month').isin([12, 1, 2])]
        elif season == 2:
            df = df[df.index.get_level_values('Month').isin([3, 4, 5])]
        elif season == 3:
            df = df[df.index.get_level_values('Month').isin([6, 7, 8])]
        elif season == 4:
            df = df[df.index.get_level_values('Month').isin([9, 10, 11])]
        else:
            print('Invalid quarter. Please restart the program and enter 1 to 4 for a season .')
            return
        
    # Perform analysis based on user inputs
    df_enhanced = analyze_data(df)

    # Plot energy comsumption data
    plot_energy_consumption(df)

if __name__ == '__main__':
    main()