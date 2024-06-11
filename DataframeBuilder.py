import pandas as pd
import numpy as np
import regex
from datetime import datetime as date


df_EConsumption = pd.read_csv('Retail_sales_of_electricity.csv', header = 4, sep=',')
df_NGConsumption = pd.read_excel('NG_CONS_SUM_A_EPG0_VGT_MMCF_M.xls', sheet_name=1, header=2)
dfHDD = pd.read_csv('MER_T01_10.csv', sep = ',')
dfCDD = pd.read_csv('MER_T01_11.csv', sep = ',')


# Data wrangling NG Consumption dataframe


df_NGConsumption.columns = df_NGConsumption.columns.map(lambda x: str.replace(x, ' (Including Vehicle Fuel) (MMcf)', '')) #modify header row 
df_NGConsumption.columns = df_NGConsumption.columns.map(lambda x: str.replace(x, 'Natural Gas Delivered to Consumers in ', '')) #modify header row
df_NGConsumption = df_NGConsumption.melt(id_vars = ['Date'], var_name='State', value_name='Natural Gas Consumption (MMcf)') #melt dataframe into long shape


# Data wrangling EG Consumption dataframe

# print(df_EConsumption['description'].unique())
df_EConsumption = df_EConsumption[df_EConsumption['description'].str.contains('all sectors')] #filter by 'all sectors' (giving us total consumption by State by Date)
df_EConsumption['description'] = df_EConsumption['description'].apply(lambda x: str.replace(x, ' : all sectors', '')) #clean descriptions column


df_EConsumption = df_EConsumption.reset_index()
df_EConsumption_Dates = np.array(df_EConsumption.columns[4:])
df_EConsumption = df_EConsumption.melt(id_vars = ['description'], var_name="Date", value_vars = df_EConsumption_Dates, value_name='Electrical Consumption (million kWh)')
df_EConsumption['Date'] = df_EConsumption['Date'].apply(lambda x: date.strptime(x, '%b %Y'))

# print(df_EConsumption.head(10))
# print(df_NGConsumption.head(10))

dfCDD['Description'] = dfCDD['Description'].apply(lambda x: str.replace(x, 'Cooling Degree-Days, ', ''))
dfCDD['Year'] = dfCDD['YYYYMM'].apply(lambda x: str(x)).str.slice(0,4).apply(lambda x: int(x))
dfCDD['Month'] = dfCDD['YYYYMM'].apply(lambda x: str(x)).str.slice(4,6).apply(lambda x: int(x))
dfCDD = dfCDD[dfCDD['Month']<=12]
dfCDD = dfCDD.reindex(columns=['Description', 'Year', 'Month', 'Value']).rename(columns = {'Description': 'Region'})
dfCDD['Degree Day'] = 'Cooling'


dfHDD['Description'] = dfHDD['Description'].apply(lambda x: str.replace(x, 'Heating Degree-Days, ', ''))
dfHDD['Year'] = dfHDD['YYYYMM'].apply(lambda x: str(x)).str.slice(0,4).apply(lambda x: int(x))
dfHDD['Month'] = dfHDD['YYYYMM'].apply(lambda x: str(x)).str.slice(4,6).apply(lambda x: int(x))
dfHDD = dfHDD[dfHDD['Month']<=12]
dfHDD = dfHDD.reindex(columns=['Description', 'Year', 'Month', 'Value']).rename(columns = {'Description': 'Region'})
dfHDD['Degree Day'] = 'Heating'




