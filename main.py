from src.DataframeBuilder import build_data_frame
from src.analysis import analyze_data
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

    # Ask user for date input
    year_input = input("Do you want to analyze a specific year or a range")

    # Perform analysis based on user inputs

    # Plot energy comsumption data

if __name__ == '__main__':
    main()