# The Cool Company - US Energy Analysis Tool

TODO: add small section on what README covers and point readers to README to cover details on how to use the tool. This markdown file should serve as supplemental documentation further explaining the decisions made behind designing the tool. A section here will also explain how this tool can be further expanded with additional functionality and analysis.

### INTRODUCTION
This tool's intended use is to summarize statistics for Natural Gas and Electrical consumption in the United States. In addition to consumption data, weather data in the form of population weighted degree day is included in the analysis for users to better understand the correlation between weather and energy consumption. 

### DATA SOURCES

**Data Source Description and Implementation**
Energy data was retrieved from the US Department of Energy. Due to the limited scope of this tool, only Natural Gas and Electricity consumption data was used for our analysis. However, with more time and resources, this tool could be expanded to include analytics for other energy sources such as Nuclear, Solar, Wind, and Biofuels. These data sets are all available from the U.S. Energy Information Administration (EIA). For our analysis, we selected Natural Gas and Electrical power demand because they make up the majority of US energy consumption in both residential, commerical, and industrial use cases. Furthermore, this data is expected to be highly correlated with weather data. Even though we can predict with a great degree of accuracy that weather data is highly correlated to energy consumption, we decided to include weather data in our analysis as it would provide an excellent, highly correlated variable for modeling and regression. Further expansion of this tool could include building a regression model that allows us to predict the short term energy consumption forecast, given a short term weather forecast. For this project, instead of selecting datasets and finding relationships, we decided to choose data that was likely to be highly correlated and show that our hypothesis was correct. In addition to this, it allows us to show that these data sets have uses that extend past the scope of this project. This would allow us to model the demand side of US energy markets. If data was available for supply side, it would then be possible to create an encompassing supply and demand model for US natural gas and electricity markets.

**Natural Gas Consumption**
TODO: ADD SECTION

**Electricity Consumption**
TODO: ADD SECTION

**Weather - Degree Day**
TODO: ADD SECTION


### DATA HANDLING
TODO: ADD SECTION ON HOW DATAFRAMES WERE BUILT AND IMPLEMENTATION OF MASTER DATA TABLE

### USER INTERFACE INPUT/OUTPUT
TODO: ADD FLOW CHART INDICATING PROCESS FLOW FOR USER INPUT AND EXPECTED OUTPUT 
**INPUT/OUTPUT Process Flow Diagram**

### CODE IMPLEMENTATION CHECKLIST
TODO: ADD SECTION ON HOW ANALYSIS WAS IMPLEMENTED, MATPLOTLIB, WHY CERTAIN ANALYTICS ARE PROVIDED AND WHY IT IS REASONABLE TO DO IT THAT WAY



