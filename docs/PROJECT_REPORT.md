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

**Data Handling: Natural Gas Consumption**<br>
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

**Data Handling: Electricity Consumption**<br>
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

**Data Handling: Degree Day Consumption**<br>
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

**INPUT/OUTPUT Process Flow Diagram**<br>
![Input/Output Diagram](https://github.com/ENSF-692-Spring-2024/ensf-692-project-the-cool-company/blob/main/screenshots/screenshot_5_inputoutput.png "Input/Output Diagram")

The above diagram contains the process flow for user inputs and program outputs for the analytics tool. Upon initial execution, the program outputs general aggregated statistics for the Contiguous United States. This includes:
    - General aggregated statistics for the dataframe using pd.describe()
    - Average Monthly Consumption and Degree Days by Month
    - Average Monthly Consumption and Degree Days by Season

Following the display of these general statistics, user input is requested for specific analytics. Please note that anytime the user enters an invalid input, an error message is returned to the user and the program is terminated. Based on the user input, the analytics functions are called to deliver the results.

## ANALYTICS

### Introduction - Analysis
In the analysis portion of our program, we have opted to generate the following statistics for output: <br>
- General aggregated statistics for the dataframe using pd.describe()
- Total Energy Consumption (million kWh)
- Average Monthly Consumption and Degree Days by Month
- Average Monthly Consumption and Degree Days by Season

Although many other statistical summaries can be provided to the user, we felt that this general summary would provide the most useful information to the user. Before completing our analysis, it was already clear that weather was highly correlated with energy consumption. To complete our project requirements - instead of selecting datasets where the relationship between the data was unclear, we have opted to select data that is highly correlated because it would create a clear path forward for further development. Due to the limited scope of the project, as well as the limited time and resources, it was unreasonable to expand the development of this tool to include regressional models, as well as predictive modeling. However, this is something that our team has discussed and outlined the opportunities for further development. <br>


### Analysis Implementation
On each execution of our program (main.py), we have provided a set of general, aggregated statistics for our dataset. The first information displayed to the user applies the pd.describe() function to the master dataframe which generates a general set of aggregated statistics for the dataset. Although not providing the user with much specialized information, it gives a good sample of the data included in the dataset, to give the user an idea of what exists. <br>

Following this information, another dataframe is printed to the output. This dataframe contains the 'Total Energy Consumption (million kWh)' column. This column was generated by taking the product of the 'Natural Gas Consumption (MMcf)' column and the natural gas energy density. This natural gas energy density value was retrieved from the EIA, and allows us to convert a volume of natural gas into an energy equivalent. After doing this, the 'Total Energy Consumption (million kWh)' can be generated by taking the sum of 'Natural Gas Energy Consumption (million kWh)' and 'Electrical Consumption (million kWh)'. <br>

```
# From Analysis.py file
# lines 10-14

natural_gas_energy_density = 0.303634232 # million kWh per 1 MMcf, from EIA conversion calculator. assuming natural gas is in standard volume
df['Natural Gas Energy Consumption (million kWh)'] = df['Natural Gas Consumption (MMcf)']*natural_gas_energy_density 
df['Total Energy Consumption (million kWh)'] = df['Natural Gas Energy Consumption (million kWh)']+df['Electrical Consumption (million kWh)']
df['Electrical/Natural Gas Consumption Ratio'] = df['Electrical Consumption (million kWh)'] / df['Natural Gas Energy Consumption (million kWh)']
print(df)
```

In the next step of the analysis, the pd.pivot_table() function is used to obtain aggregate values for the total natural gas consumption over the time range in our dataset. Using this pivot table, we are able to generate and print the aggregate values for total consumption.

```
# From Analysis.py file
# lines 17-26

new_df = df.pivot_table("Natural Gas Consumption (MMcf)", index=["Month"], columns=["Year"])

df["DateTime"] = df.index.get_level_values('Year').astype(str) + '-' + df.index.get_level_values('Month').astype(str)
df["DateTime"] = pd.to_datetime(df["DateTime"], format="%Y-%m")

total_energy_df = df.pivot_table("Total Energy Consumption (million kWh)", index=["DateTime"])
elec_consumption_df = df.pivot_table('Electrical Consumption (million kWh)', index = ['DateTime'])
natural_gas_energy_df = df.pivot_table('Natural Gas Energy Consumption (million kWh)', index = ['DateTime'])
dd_df = df.pivot_table('DD', index = ['DateTime'])
df_year = df.pivot_table("Total Energy Consumption (million kWh)", index = 'Month', columns = 'Year')
```

The next part of the analysis consisted of printing the 'Average Monthly Consumption and Degree Days by Month' and the 'Average Monthly Consumption and Degree Days by Season'. This is done by using the pd.group_by() function.

```
# From Analysis.py file
# lines 38-56

# Average Monthly Consumption by Month
print('\n'*2)
print('******** Average Monthly Consumption and Degree Days by Month ********')
grouped_months_natural_gas_df = df.groupby('Month')['Natural Gas Consumption (MMcf)'].mean()
grouped_months_electricity_df = df.groupby('Month')['Electrical Consumption (million kWh)'].mean()
grouped_months_total_energy_df = df.groupby('Month')['Total Energy Consumption (million kWh)'].mean()
grouped_months_degree_days_df = df.groupby('Month')['DD'].mean()
grouped_months_df = pd.DataFrame({'Natural Gas Consumption (MMcf)':grouped_months_natural_gas_df, 'Electrical Consumption (million kWh)':grouped_months_electricity_df, 'Total Energy Consumption (million kWh)': grouped_months_total_energy_df, 'Degree Days': grouped_months_degree_days_df})
print(grouped_months_df)

# Average Monthly Consumption by Season
print('\n' * 2)
print('******** Average Monthly Consumption and Degree Days by Season ********')
winter_averages = grouped_months_df.loc[[12, 1, 2]].mean()
spring_averages = grouped_months_df.loc[[3, 4, 5]].mean()
summer_averages = grouped_months_df.loc[[6, 7, 8]].mean()
fall_averages = grouped_months_df.loc[[9, 10, 11]].mean()
seasonal_averages = pd.DataFrame({'Winter': winter_averages, 'Spring': spring_averages, 'Summer': summer_averages, 'Fall': fall_averages}).transpose()
print(seasonal_averages)
```

After the general analytics are generated, the input/output portion of the Main.py file is executed.

### Data Visualization and Plots
#### General Visualizations
To visualize the data, several plots are generated. Three plots are generated based on aggregated data, which can be found below. <br>

**Figure 1. Energy Consumption Over Time For Contiguous US**
![Figure 1.](https://github.com/ENSF-692-Spring-2024/ensf-692-project-the-cool-company/blob/main/plots/energy_consumption_over_time.png "Figure 1.")
<br>

**Figure 2. Degree Days Over Time For Contiguous US**
![Figure 2.](https://github.com/ENSF-692-Spring-2024/ensf-692-project-the-cool-company/blob/main/plots/degree_days_over_time.png "Figure 2.")
<br>

**Figure 3. Monthly Energy Consumption for Contiguous US vs. Degree Days**
![Figure 3.](https://github.com/ENSF-692-Spring-2024/ensf-692-project-the-cool-company/blob/main/plots/consumption_vs_ddays.png "Figure 3.")
<br>

These three figures provide a general visualization for our data. **Figure 1** contains the monthly electrical, natural gas, and total energy consumption for the Contiguous United States. From **Figure 1**, we can observe that natural gas consumption (demand) has increased over time, with consumption seeming to increase at a greater rate after 2012. Please note, this is simply and observation, and reasons behind this increase would have to be analyzed further. Peaks in natural gas consumption and electricity consumption appear to offset each other. This is because natural gas demand primarly peaks in the winter months when gas demand increases for heating purposes. Conversely, electricity demand peaks in the summer, which may be to be due to electrical consumption for cooling purposes such as air conditioning.
<br>

Deeper analysis into energy consumption can be completed but is not within the scope of this tool and would require more granular datasets, which can be obtained from EIA. <br>

**Figure 2** contains a monthly time-series visualization of Degree Days. To understand this figure, the definition of 'degree days' must be understood, which is explained in the section explaining Data Sources (Weather - Degree Day). The data retrieved from the EIA contains weather data around a base 65°F. For our visualization, this means that any positive value, represents degree days over 65°F, and any degree days below base 65°F. This is needed to be done to better visualize weather because the values for Cooling Degree Days and Heating Degree Days both come in as positive values. Looking at the figure, we can see that it oscillates, which is expected due to the cyclical nature of weather. In fact, there seems to be an inflection point indicating the warming and cooling of the seasons. <br>

**Figure 3** visualizes Degree Days on the x-axis, and Total Energy Consumption on the y-axis. To generate this graph, energy consumption is grouped by month. This visualization allows the user to understand the relationship between degree days and total energy consumption. Based on the data, we find that there are more data points in the positive portion of the x-axis. This makes sense, as summer appears to be the only time of the year where degree days are negative, indicating that the daily average temperature is below 65°F only in the summer.

#### User Input Generated Plots
Our tool generates three plots based on user input. These plots are generated based on user input, and are generated automatically for a specificed region, with data points appearing on seasonal or monthly time-series based on user input. This allows the tool user to visualize their data for a specific region, over time. Please refer to the following three figures, which provides an example of the output when the user specifies the region to be "New England", and on a "season" basis. Note, this is why the data points do not line up perfectly with the year. 

![Absolute Degree Days - New England](https://github.com/ENSF-692-Spring-2024/ensf-692-project-the-cool-company/blob/main/plots/absolute_degree_days.png "Absolute Degree Days")
<br>

![Natural Gas Consumption - New England](https://github.com/ENSF-692-Spring-2024/ensf-692-project-the-cool-company/blob/main/plots/natural_gas_consumption.png "Natural Gas Consumption")
<br>

![Electrical Consumption - New England](https://github.com/ENSF-692-Spring-2024/ensf-692-project-the-cool-company/blob/main/plots/electrical_consumption.png "Electrical Consumption")
<br>


## FUTURE ANALYTICS

As mentioned previously in the Introduction - Analytics section of this report, further analytics can be completed, but were not done in this implementation. With more resources, the scope of the tool could be expanded. <br>

One very useful application would be to complete a seasonal time series analysis on a training set of the data. This regression could be done on the entire Contiguous United States. However, the best use case for this would be to create models for each 'State' or 'Region'. This model would ideally be trained on day of the year, and degree day. This would allow for us to implement the model and feed it with a weather forecast for days ahead to generate a forecasted demand for each region or state. <br>

More functionality could also be added to the tool in order to create comparisons between the demand profile of different states. Also, demand from other sources of energy could be integrated into this model in order to create a more robust and inclusive analytics tool for energy demand in the Contiguous United States. <br>

In the end, a dashboard could be generated, producing many different displays for different visualizations of this data so that the enduser would better understand the natural gas and electricity demand markets for the Contiguous United States.



