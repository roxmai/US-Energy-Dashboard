# The Cool Company - US Energy Analysis Tool

TODO: add small section on what README covers and point readers to README to cover details on how to use the tool. This markdown file should serve as supplemental documentation further explaining the decisions made behind designing the tool. A section here will also explain how this tool can be further expanded with additional functionality and analysis.

## INTRODUCTION
This tool's intended use is to summarize statistics for Natural Gas and Electrical consumption in the United States. In addition to consumption data, weather data in the form of population weighted degree day is included in the analysis for users to better understand the correlation between weather and energy consumption. 

## DATA SOURCES AND DATA HANDLING

### Data Source Description and Implementation
Energy data was retrieved from the US Department of Energy. Due to the limited scope of this tool, only Natural Gas and Electricity consumption data was used for our analysis. However, with more time and resources, this tool could be expanded to include analytics for other energy sources such as Nuclear, Solar, Wind, and Biofuels. These data sets are all available from the U.S. Energy Information Administration (EIA). For our analysis, we selected Natural Gas and Electrical power demand because they make up the majority of US energy consumption in both residential, commerical, and industrial use cases. Furthermore, this data is expected to be highly correlated with weather data. Even though we can predict with a great degree of accuracy that weather data is highly correlated to energy consumption, we decided to include weather data in our analysis as it would provide an excellent, highly correlated variable for modeling and regression. Further expansion of this tool could include building a regression model that allows us to predict the short term energy consumption forecast, given a short term weather forecast. For this project, instead of selecting datasets and finding relationships, we decided to choose data that was likely to be highly correlated and show that our hypothesis was correct. In addition to this, it allows us to show that these data sets have uses that extend past the scope of this project. This would allow us to model the demand side of US energy markets. If data was available for supply side, it would then be possible to create an encompassing supply and demand model for US natural gas and electricity markets.

### Natural Gas Consumption
[Natural Gas Consumption]("https://www.eia.gov/dnav/ng/ng_cons_sum_a_EPG0_vgt_mmcf_m.htm") data was retrieved from the US Department of Energy, Energy Information Administration (EIA) website. This source contains a large repository of energy data and related economic data. This federal agency collects, analyzes, and deseminates information, providing the public with independent and impartial energy information. There are many repositories of data including both supply side, and demand side data. The website shares information regarding US natural gas imports and exports, as well as production, split by many different categories such as port of entry, state, imports and exports by country. For our analysis, we are focusing only on natural gas demand in the Contiguous United States. A screenshot of the natural gas consumption data can be found below:

![Natural Gas Consumption Data](https://github.com/ENSF-692-Spring-2024/ensf-692-project-the-cool-company/blob/main/screenshots/screenshot_2_natgasconsumption.png "EIA Natural Gas Consumption Data")

**Data Handling: Natural Gas Consumption**
Please refer to "DataframeBuilder.py" for the data handling code. In order to wrangle the natural gas consumption data into the desired format, string cleaning was first performed on the column names to extract the state names. The data was then converted to long format by applying a melt function. Extraneous data had to be removed by applying a mask, filtering out total US consumption and The District of Columbia (not technically a state). Following this, a dictionary containing {'US Census Region': 'State'} data was mapped to the 'States' column. Lastly, using a string index slice, the month and year were extracted into their respective columns from the 'Date' column, which originally had the format of 'Jan-2001', for example.

```
# Natural Gas Consumption dataframe wrangling
# from DataframeBuilder.py, line 25-34

df_NGConsumption.columns = df_NGConsumption.columns.map(lambda x: str.replace(x, ' (Including Vehicle Fuel) (MMcf)', '')) #modify header row 
df_NGConsumption.columns = df_NGConsumption.columns.map(lambda x: str.replace(x, 'Natural Gas Delivered to Consumers in ', '')) #modify header row
df_NGConsumption = df_NGConsumption.melt(id_vars = ['Date'], var_name='State', value_name='Natural Gas Consumption (MMcf)') #melt dataframe into long shape
df_NGConsumption = df_NGConsumption[df_NGConsumption['State'] != 'the U.S. (MMcf)'] #remove US data
df_NGConsumption = df_NGConsumption[df_NGConsumption['State'] != 'the District of Columbia'] #removed District of Columbia (not technically a state)
df_NGConsumption['Region'] = df_NGConsumption['State'].map(regions_dict) #map regions to states using regions_dict dictionary
df_NGConsumption['Year'] = df_NGConsumption['Date'].apply(lambda x: str(x)).str.slice(0,4).apply(lambda x: int(x)) #extract 'Year' from date column and cast to int
df_NGConsumption['Month'] = df_NGConsumption['Date'].apply(lambda x: str(x)).str.slice(5,7).apply(lambda x: int(x)) #extract 'Month' from year column and cast to int
df_NGConsumption = df_NGConsumption.reindex(columns=['Region', 'State', 'Year', 'Month', 'Natural Gas Consumption (MMcf)']) #select and ordering column
```

### Electricity Consumption
[Electrical Consumption]("https://www.eia.gov/electricity/data/browser/#/topic/5?agg=0,1&geo=vvvvvvvvvvvvo&linechart=ELEC.SALES.TX-ALL.M~ELEC.SALES.TX-RES.M~ELEC.SALES.TX-COM.M~ELEC.SALES.TX-IND.M&columnchart=ELEC.SALES.TX-ALL.M~ELEC.SALES.TX-RES.M~ELEC.SALES.TX-COM.M~ELEC.SALES.TX-IND.M&map=ELEC.SALES.US-ALL.M&freq=M&start=200101&end=202403&ctype=linechart&ltype=pin&rtype=s&maptype=0&rse=0&pin=&endsec=vg") data was also retrieved from the EIA website. This electricity consumption data contains the total monthly retail sales of electricity by State, starting from January 2001 up to March 2024. A screenshot of the electricity consumption data can be seen below:

![Electricity Consumption Data](https://github.com/ENSF-692-Spring-2024/ensf-692-project-the-cool-company/blob/main/screenshots/screenshot_3_electricityconsumption.png "EIA Electricity Consumption Data")

**Data Handling: Electricity Consumption**
In order to wrangle the electricity consumption data into the desired format, the 'description' column was filtered using a mask to find all instances of a string that contains 'all sectors' in the string. This was done because the data table contains electricity consumption data to multiple sectors, where we are only interested in all sectors. After applying the mask, cleaning was performed on the 'description', column using str.replace to extract the State name. The pd.melt function was then utilized to convert the data into long format. The region dictionary was mapped to the data in order to match Census regions to States. The same str.slice method was then used to extract the 'Year' and 'Month' from the 'Date' column. 
Finally, the column name for 'description' was changed to 'State' and then reindexed to the correct order to prepare for merging.

```
# Electricity Consumption dataframe wrangling
# from DataframeBuilder.py, line 37-49

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
```

### Weather - Degree Day
[HDD Data]("https://www.eia.gov/totalenergy/data/browser/index.php?tbl=T01.10#/?f=M&start=197301&end=202402&charted=32-10")
[CDD Data]("https://www.eia.gov/totalenergy/data/browser/index.php?tbl=T01.11#/?f=M&start=197301&end=202402&charted=32-10")

For weather, degree day data was also retrieved from the EIA website, however, the original source of this data National Weather Service, Climate Prediction Center. Degree days are typically used to estimate energy requirements for heating and cooling buildings. A degree day provides a measure of how much the outside temperature deviates from a standard base temperature, typically 65°F (18°C). When the temperature rises above 65°F, the degree day is called a 'Cooling Degree Day', because energy will be used for cooling. Conversely, when the temperature is below the base value of 65°F, the degree day is called a 'Heating Degree Day'. We use degree days because daily high and lows only capture a range of temperature and does not incorporate a time factor. Degree days captures the weather changes over a daily period, effectively providing a measure of temperature over a period of time. In our case, the data source used captures degree days over a monthly period. Additionally, this data is population weighted by US Census Regions. This is why the Census Regions was mapped to the contiguous US states.

Degree Day data which is expected to be highly correlated with consumption, provides us with a parameter that can be used as predictive variable that can be used for regression modeling, therefore, the natural gas demand and electricity demand can be predicted given a forward looking weather forecast. This is why the relationship between weather and natural gas demand is highly important.

A screenshot of the HDD weather data can be found below. Note, that CDD data was also wrangled using an identical process because they came in as consistent formats.

![HDD Weather Data](https://github.com/ENSF-692-Spring-2024/ensf-692-project-the-cool-company/blob/main/screenshots/screenshot_4_HDD.png "HDD Weather Data")

**Data Handling: Degree Day Consumption**
To wrangle the degree day data, the 'Description' column was cleaned to extract the State from the column. Using the str.slice function, is used to extract the month and year from the 'YYYYMM' column. The columns are the reindexed and the a mask is aplied to remove the aggregated data from the 'Region' column.

```
# HDD Data dataframe wrangling
# from DataframeBuilder.py, line 60-65

dfHDD['Description'] = dfHDD['Description'].apply(lambda x: str.replace(x, 'Heating Degree-Days, ', '')) #clean up description string
dfHDD['Year'] = dfHDD['YYYYMM'].apply(lambda x: str(x)).str.slice(0,4).apply(lambda x: int(x)) #extract year from YYYYMM and cast to int
dfHDD['Month'] = dfHDD['YYYYMM'].apply(lambda x: str(x)).str.slice(4,6).apply(lambda x: int(x)) #extract month from YYYYMM ad cast to int
dfHDD = dfHDD[dfHDD['Month']<=12] #filter 'Month' column to only include month data. Note that a 13th month is the total HDD across a year
dfHDD = dfHDD.reindex(columns=['Description', 'Year', 'Month', 'Value']).rename(columns = {'Description': 'Region', 'Value': 'HDD'}) #select and ordering columns
dfHDD = dfHDD[dfHDD['Region'] != 'United States'] #filter to remove total US from 'Region column
```

### Master Dataframe
After wrangling the dataframes generated from the data sources, the master dataframe is generated by using the merge function on each dataframe. In addition, a new column is created to reflect the total degree days called 'DD'. This allows us to represent the degree day data around a base of 65°F. Lastly, a hierarchical index is created on 'Region', 'State', 'Year', and 'Month'. This is all wrapped into a function called build_data_frame() which returns the master dataframe. This dataframe consists of 4 merged datasets with a totel of 13344 rows for analytics.

```
# Master Dataframe building
# from DataframeBuilder.py, line 68-70

df = df_NGConsumption.merge(df_EConsumption).merge(dfHDD).merge(dfCDD)
df['DD'] = df['HDD'] - df['CDD'] #create new column with total degree days (energy used for heating is positive)
df = df.set_index(['Region', 'State', 'Year', 'Month'])
``` 

## USER INTERFACE INPUT/OUTPUT

Please refer to main.py for the code that manages user inputs and outputs, as well as the overall implementation of the tool. 

**INPUT/OUTPUT Process Flow Diagram**
![Input/Output Diagram](https://github.com/ENSF-692-Spring-2024/ensf-692-project-the-cool-company/blob/main/screenshots/screenshot_5_inputoutput.png "Input/Output Diagram")

The above diagram contains the process flow for user inputs and program outputs for the analytics tool. Upon initial execution, the program outputs general aggregated statistics for the Contiguous United States. This includes:
    - General aggregated statistics for the dataframe using pd.describe()
    - Average Monthly Consumption and Degree Days by Month
    - Average Monthly Consumption and Degree Days by Season

Following the display of these general statistics, user input is requested for specific analytics. Please note that anytime the user enters an invalid input, an error message is returned to the user and the program is terminated. Based on the user input, the analytics functions are called to deliver the results.

## ANALYTICS


### CODE IMPLEMENTATION CHECKLIST
TODO: ADD SECTION ON HOW ANALYSIS WAS IMPLEMENTED, MATPLOTLIB, WHY CERTAIN ANALYTICS ARE PROVIDED AND WHY IT IS REASONABLE TO DO IT THAT WAY



