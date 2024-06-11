import pandas as pd
import numpy as np
import regex
from datetime import datetime as date

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

df_EConsumption = pd.read_csv('Retail_sales_of_electricity.csv', header = 4, sep=',')
df_NGConsumption = pd.read_excel('NG_CONS_SUM_A_EPG0_VGT_MMCF_M.xls', sheet_name=1, header=2)
dfHDD = pd.read_csv('MER_T01_10.csv', sep = ',')
dfCDD = pd.read_csv('MER_T01_11.csv', sep = ',')

# Data wrangling NG Consumption dataframe
df_NGConsumption.columns = df_NGConsumption.columns.map(lambda x: str.replace(x, ' (Including Vehicle Fuel) (MMcf)', '')) #modify header row 
df_NGConsumption.columns = df_NGConsumption.columns.map(lambda x: str.replace(x, 'Natural Gas Delivered to Consumers in ', '')) #modify header row
df_NGConsumption = df_NGConsumption.melt(id_vars = ['Date'], var_name='State', value_name='Natural Gas Consumption (MMcf)') #melt dataframe into long shape
df_NGConsumption = df_NGConsumption[df_NGConsumption['State'] != 'the U.S. (MMcf)']
df_NGConsumption = df_NGConsumption[df_NGConsumption['State'] != 'the District of Columbia']
df_NGConsumption['Region'] = df_NGConsumption['State'].map(regions_dict)
df_NGConsumption = df_NGConsumption.reindex(columns=['Region', 'State', 'Date', 'Natural Gas Consumption (MMcf)'])

# Data wrangling EG Consumption dataframe
df_EConsumption = df_EConsumption[df_EConsumption['description'].str.contains('all sectors')] #filter by 'all sectors' (giving us total consumption by State by Date)
df_EConsumption['description'] = df_EConsumption['description'].apply(lambda x: str.replace(x, ' : all sectors', '')) #clean descriptions column
df_EConsumption = df_EConsumption.reset_index()
df_EConsumption_Dates = np.array(df_EConsumption.columns[4:])
df_EConsumption = df_EConsumption.melt(id_vars = ['description'], var_name="Date", value_vars = df_EConsumption_Dates, value_name='Electrical Consumption (million kWh)')
df_EConsumption['Date'] = df_EConsumption['Date'].apply(lambda x: date.strptime(x, '%b %Y'))
df_EConsumption = df_EConsumption[df_EConsumption['description'].isin(list(regions_dict.keys()))]
df_EConsumption['Region'] = df_EConsumption['description'].map(regions_dict)
df_EConsumption = df_EConsumption.reindex(columns=['Region', 'description', 'Date', 'Electrical Consumption (million kWh)'])
df_EConsumption = df_EConsumption.rename(columns = {'description': 'State'})

# Data wrangling CDD dataframe
dfCDD['Description'] = dfCDD['Description'].apply(lambda x: str.replace(x, 'Cooling Degree-Days, ', ''))
dfCDD['Year'] = dfCDD['YYYYMM'].apply(lambda x: str(x)).str.slice(0,4).apply(lambda x: int(x))
dfCDD['Month'] = dfCDD['YYYYMM'].apply(lambda x: str(x)).str.slice(4,6).apply(lambda x: int(x))
dfCDD = dfCDD[dfCDD['Month']<=12]
dfCDD = dfCDD.reindex(columns=['Description', 'Year', 'Month', 'Value']).rename(columns = {'Description': 'Region'})
dfCDD['Degree Day'] = 'Cooling'

# Data wrangling HDD dataframe
dfHDD['Description'] = dfHDD['Description'].apply(lambda x: str.replace(x, 'Heating Degree-Days, ', ''))
dfHDD['Year'] = dfHDD['YYYYMM'].apply(lambda x: str(x)).str.slice(0,4).apply(lambda x: int(x))
dfHDD['Month'] = dfHDD['YYYYMM'].apply(lambda x: str(x)).str.slice(4,6).apply(lambda x: int(x))
dfHDD = dfHDD[dfHDD['Month']<=12]
dfHDD = dfHDD.reindex(columns=['Description', 'Year', 'Month', 'Value']).rename(columns = {'Description': 'Region'})
dfHDD['Degree Day'] = 'Heating'

print(df_NGConsumption.head(10))
print(df_EConsumption.head(10))
# print(df_NGConsumption['State'].unique())
# print(list(regions_dict.keys()))
# print(df_EConsumption['description'].unique())
# print(dfCDD['Region'].unique())