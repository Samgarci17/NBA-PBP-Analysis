# NBA-PBP-Analysis 

## Overview
A look through the play-by-play data from NBA playoffs years 1997-2024, looking at trends in leads.

## Data
The data used in this analysis was scraped from [Basketball Reference](https://www.basketball-reference.com/playoffs/series.html) using my Python script containing the BS4, request, and pandas modules. Some simple calculations were done on the play-by-play tables to track the largest lead of each game and the largest comeback. The data was stored in Pandas DataFrames and then saved in CSV format using the Pandas to_csv function.

## Tools and Libraries

- Python (pandas, numpy, scipy.stats, matplotlib)
- Jupyter Notebook 

## Analysis Process
Explain the general steps of your analysis:
1. Data cleaning and preprocessing - The only step taken to clean and process the data was removing the missing values at the bottom of each data frame column.
   
2. Exploratory Data Analysis (EDA) - To get a summary of the data descriptive statistics were calculated such as the mean, median, and standard deviation. All three descriptive statistics were found for the Leads data frame as well as the individual mean of each column. Another approach was taken for the comeback data frame, the number of games without a lead change was calculated to be used in further visualization.
   
3. Data visualization - A plot was created for the lead and comeback data frames to identify seasons of interest that should be explored more deeply. The plot of the leads data frame plotted the mean of each column against each year. The plot from the comeback data frame plotted the average number of games without a lead change over each year. <p></p> These two plots showed a general trend of leads increasing in size over the years while the number of games without a lead change was relatively constant. When analyzing individual seasons histograms were created for each of the seasons of interest to look at the skew and distribution of those seasons compared to the average.
   
4. Statistical analysis or modeling - The two that stood out as significant from the years graphed with histograms were the 2016 and 2018 seasons. To test if these seasons were significant a one-sample T-test was used and produced the result of T-statistic: 2.486945239867086 and a P-value: 0.014839514258574603 for the 2016 playoffs. Then the 2008 and 2011 seasons were tested as they were visually distinct on the mean summary plot and the 2011 playoffs produced T-statistic: -4.0049773273438305 and a P-value: 0.00013800162357397887.
   
5. Results interpretation - The goal of the analysis was to identify lead trends in the postseason and if leads have been influenced by the influx of high-scoring games and if there is more volatility in the strength of a large lead. The results clearly show a positive correlation between the increase in scoring and the size of leads increasing. With the size of leads increasing the safety of those leads has not. Possibly due to the ease of scoring but leads are just as likely to be erased now as they were in the past even though they are noticeably larger on average. 


## Results
Summarize the key findings from your analysis. Include any visuals or links to relevant documents.

## How to Run
Provide instructions on how to set up and run the project:
