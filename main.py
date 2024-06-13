from DataframeBuilder import build_data_frame
from analysis import analyze_data
import numpy as np
import pandas as pd

# def main():
    # build the dataframe using the provided function
df = build_data_frame()

# Ask user for region input
region_input = input("Enter region that you want analysis? (e.g. East North Central):").strip().lower()

# Ask user for date input
year_input = input("Do you want to analyze a specific year or a range")

# Perform analysis based on user inputs

# Plot energy comsumption data

# if __name__ == '__main__':
#     main()