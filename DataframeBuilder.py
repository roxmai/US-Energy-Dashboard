import pandas as pd
import numpy as np
import datetime as date


df_EConsumption = pd.read_csv('Retail_sales_of_electricity.csv', header = 4, sep=',')
df_NGConsumption = pd.read_excel('NG_CONS_SUM_A_EPG0_VGT_MMCF_M.xls', sheet_name=1, header=2)
dfHDD = pd.read_csv('MER_T01_10.csv', sep = ',')
dfCDD = pd.read_csv('MER_T01_11.csv', sep = ',')

# Modify header row in NG Consumption dataset

df_NGConsumption.columns = df_NGConsumption.columns.map(lambda x: str.replace(x, ' (Including Vehicle Fuel) (MMcf)', ''))
df_NGConsumption.columns = df_NGConsumption.columns.map(lambda x: str.replace(x, 'Natural Gas Delivered to Consumers in ', ''))
df_NGConsumption = df_NGConsumption.melt(id_vars = ['Date'], var_name='State', value_name='Natural Gas Consumption (MMcf)')

# print(df_NGConsumption.head(15))
print(df_NGConsumption.dtypes)


