# NBA-PBP-Analysis 

## Overview
A look through the play-by-play data from NBA playoffs years 1997-2024, looking at trends in leads and comebacks.

## Table of Contents
- [Project Overview](#overview)
- [Data](#data)
- [Tools and Libraries](#tools-and-libraries)
- [Analysis Process](#analysis-process)
- [Results](#results)
- [How to Run](#how-to-run)
- [Contributions](#contributions)
- [License](#license)

## Data
The data used in this analysis was scraped from [Basketball Reference](https://www.basketball-reference.com/playoffs/series.html) using my Python script containing the BS4, request, and pandas modules. Some simple calculations were done on the play-by-play tables to track the largest lead of each game and the largest comeback. The data was stored in Pandas DataFrames and then saved in CSV format using the Pandas to_csv function.

## Tools and Libraries

- Python (pandas, numpy, scipy.stats, matplotlib)
- Jupyter Notebook 

## Analysis Process
Explain the general steps of your analysis:
1. Data cleaning and preprocessing - The data cleaning process consisted of handling missing values at the bottom of each data frame column
2. Exploratory Data Analysis (EDA) - In order to find the seasons of interest that should be explored more deeply a plot was created for both the leads and comeback data frames.
   These plots were created using the mean value of each year to visualize the trend of leads and comebacks over time. 
4. Data visualization
5. Statistical analysis or modeling
6. Results interpretation


## Results
Summarize the key findings from your analysis. Include any visuals or links to relevant documents.

## How to Run
Provide instructions on how to set up and run the project:
