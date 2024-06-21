import pandas as pd
import numpy as np
import regex
from datetime import datetime as date

def build_data_frame():
    '''
    Builds the master dataframe required for the energy consumption analysis tool
    ''' 

    regions_dict = {'Connecticut':'New England', 'Maine':'New England', 'Massachusetts':'New England', 'New Hampshire':'New England', 'Rhode Island':'New England', 'Vermont':'New England',
    'New Jersey':'Middle Atlantic', 'New York':'Middle Atlantic', 'Pennsylvania':'Middle Atlantic',
    'Indiana':'East North Central', 'Illinois':'East North Central', 'Michigan':'East North Central', 'Ohio':'East North Central', 'Wisconsin':'East North Central', 
    'Iowa':'West North Central', 'Kansas':'West North Central', 'Minnesota':'West North Central', 'Missouri':'West North Central', 'Nebraska':'West North Central', 
    'North Dakota':'West North Central', 'South Dakota':'West North Central', 
    'Delaware':'South Atlantic', 'District of Columbia':'South Atlantic', 'Florida':'South Atlantic', 'Georgia':'South Atlantic', 'Maryland':'South Atlantic', 
    'North Carolina':'South Atlantic', 'South Carolina':'South Atlantic', 'Virginia':'South Atlantic', 'West Virginia':'South Atlantic', 
    'Alabama':'East South Central', 'Kentucky':'East South Central', 'Mississippi':'East South Central', 'Tennessee':'East South Central',
    'Arkansas':'West South Central', 'Louisiana':'West South Central', 'Oklahoma':'West South Central', 'Texas':'West South Central', 
    'Arizona':'Mountain', 'Colorado':'Mountain', 'Idaho':'Mountain', 'New Mexico':'Mountain', 'Montana':'Mountain', 'Utah':'Mountain', 'Nevada':'Mountain', 'Wyoming':'Mountain', 
    'California':'Pacific', 'Oregon':'Pacific', 'Washington':'Pacific'}

    # IMPORT DATA
    df_EConsumption = pd.read_csv('Retail_sales_of_electricity.csv', header = 4, sep=',')
    df_NGConsumption = pd.read_excel('NG_CONS_SUM_A_EPG0_VGT_MMCF_M.xls', sheet_name=1, header=2)
    dfHDD = pd.read_csv('MER_T01_10.csv', sep = ',')
    dfCDD = pd.read_csv('MER_T01_11.csv', sep = ',')

    # DATA WRANGLING - df_NGConsumption: Natural Gas Consumption
    df_NGConsumption.columns = df_NGConsumption.columns.map(lambda x: str.replace(x, ' (Including Vehicle Fuel) (MMcf)', '')) #modify header row 
    df_NGConsumption.columns = df_NGConsumption.columns.map(lambda x: str.replace(x, 'Natural Gas Delivered to Consumers in ', '')) #modify header row
    df_NGConsumption = df_NGConsumption.melt(id_vars = ['Date'], var_name='State', value_name='Natural Gas Consumption (MMcf)') #melt dataframe into long shape
    df_NGConsumption = df_NGConsumption[df_NGConsumption['State'] != 'the U.S. (MMcf)'] #remove US data
    df_NGConsumption = df_NGConsumption[df_NGConsumption['State'] != 'the District of Columbia'] #removed District of Columbia (not technically a state)
    df_NGConsumption['Region'] = df_NGConsumption['State'].map(regions_dict) #map regions to states using regions_dict dictionary
    df_NGConsumption['Year'] = df_NGConsumption['Date'].apply(lambda x: str(x)).str.slice(0,4).apply(lambda x: int(x)) #extract 'Year' from date column and cast to int
    df_NGConsumption['Month'] = df_NGConsumption['Date'].apply(lambda x: str(x)).str.slice(5,7).apply(lambda x: int(x)) #extract 'Month' from year column and cast to int
    df_NGConsumption = df_NGConsumption.reindex(columns=['Region', 'State', 'Year', 'Month', 'Natural Gas Consumption (MMcf)']) #select and ordering column

    # DATA WRANGLING - df_EConsumption: Electricity Consumption
    df_EConsumption = df_EConsumption[df_EConsumption['description'].str.contains('all sectors')] #filter by 'all sectors' (giving us total consumption by State by Date)
    df_EConsumption['description'] = df_EConsumption['description'].apply(lambda x: str.replace(x, ' : all sectors', '')) #clean descriptions column
    df_EConsumption = df_EConsumption.reset_index() 
    df_EConsumption_Dates = np.array(df_EConsumption.columns[4:]) # get the Dates as an array to melt into long shape
    df_EConsumption = df_EConsumption.melt(id_vars = ['description'], var_name="Date", value_vars = df_EConsumption_Dates, value_name='Electrical Consumption (million kWh)') #melt function to convert from wide to long dataframe
    df_EConsumption['Date'] = df_EConsumption['Date'].apply(lambda x: date.strptime(x, '%b %Y')) #get dates into YYYY-MM-DD using datetime 
    df_EConsumption = df_EConsumption[df_EConsumption['description'].isin(list(regions_dict.keys()))] #filter 'description' on an array of US States
    df_EConsumption['Electrical Consumption (million kWh)'] = df_EConsumption['Electrical Consumption (million kWh)'].apply(lambda x: float(x)) #cast Electrical Consumption column to float
    df_EConsumption['Region'] = df_EConsumption['description'].map(regions_dict) #map region to states
    df_EConsumption['Year'] = df_EConsumption['Date'].apply(lambda x: str(x)).str.slice(0,4).apply(lambda x: int(x)) #extract year from 'Date' column and cast to int
    df_EConsumption['Month'] = df_EConsumption['Date'].apply(lambda x: str(x)).str.slice(5,7).apply(lambda x: int(x)) #extract month from 'Date' column and cast to int
    df_EConsumption = df_EConsumption.rename(columns = {'description': 'State'}) #rename 'description' to 'State'
    df_EConsumption = df_EConsumption.reindex(columns=['Region', 'State', 'Year', 'Month', 'Electrical Consumption (million kWh)']) #select and ordering columns

    # DATA WRANGLING - dfCDD: Cooling Degree Days
    dfCDD['Description'] = dfCDD['Description'].apply(lambda x: str.replace(x, 'Cooling Degree-Days, ', '')) #clean up description string
    dfCDD['Year'] = dfCDD['YYYYMM'].apply(lambda x: str(x)).str.slice(0,4).apply(lambda x: int(x)) #extract year from 'YYYYMM' and cast to int
    dfCDD['Month'] = dfCDD['YYYYMM'].apply(lambda x: str(x)).str.slice(4,6).apply(lambda x: int(x)) #extract year from 'YYYYMM' and cast to int
    dfCDD = dfCDD[dfCDD['Month']<=12] #filter 'Month' column to only include month data. Note that a 13th month is the total CDD across a year
    dfCDD = dfCDD.reindex(columns=['Description', 'Year', 'Month', 'Value']).rename(columns = {'Description': 'Region', 'Value': 'CDD'}) #select and ordering columns
    dfCDD = dfCDD[dfCDD['Region'] != 'United States'] #filter to remove total US from 'Region' column

    # DATA WRANGLING - dfHDD: Heeting Degree Days
    dfHDD['Description'] = dfHDD['Description'].apply(lambda x: str.replace(x, 'Heating Degree-Days, ', '')) #clean up description string
    dfHDD['Year'] = dfHDD['YYYYMM'].apply(lambda x: str(x)).str.slice(0,4).apply(lambda x: int(x)) #extract year from YYYYMM and cast to int
    dfHDD['Month'] = dfHDD['YYYYMM'].apply(lambda x: str(x)).str.slice(4,6).apply(lambda x: int(x)) #extract month from YYYYMM ad cast to int
    dfHDD = dfHDD[dfHDD['Month']<=12] #filter 'Month' column to only include month data. Note that a 13th month is the total HDD across a year
    dfHDD = dfHDD.reindex(columns=['Description', 'Year', 'Month', 'Value']).rename(columns = {'Description': 'Region', 'Value': 'HDD'}) #select and ordering columns
    dfHDD = dfHDD[dfHDD['Region'] != 'United States'] #filter to remove total US from 'Region column

    # JOIN DATA
    df = df_NGConsumption.merge(df_EConsumption).merge(dfHDD).merge(dfCDD)
    df['DD'] = df['HDD'] - df['CDD'] #create new column with total degree days (energy used for heating is positive)
    df = df.set_index(['Region', 'State', 'Year', 'Month'])

    # print(df.head(10))
    # print(df.describe())
    return df