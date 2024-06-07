import pandas as pd
import numpy as np

dfElectrictyConsumption = pd.read_csv('Retail_sales_of_electricity.csv', header = 4, sep=',')
dfNaturalGasConsumption = pd.read_excel('NG_CONS_SUM_DCU_NUS_M.xlsx', sheet_name=1, header=2)
dfHDD = pd.read_csv('MER_T01_10.csv', sep = ',')
dfCDD = pd.read_csv('MER_T01_11.csv', sep = ',')
print(dfCDD)