# NBA-PBP-Analysis 

## Overview
A look through the play-by-play data from NBA playoffs years 1997-2024, looking at trends in leads and comebacks.

## Table of Contents
- [Project Overview](#overview)
- [Data](#data)
- [Tools and Libraries](#tools-and-libraries)
- [File Structure](#file-structure)
- [Analysis Process](#analysis-process)
- [Results](#results)
- [How to Run](#how-to-run)
- [Contributions](#contributions)
- [License](#license)

## Data
The data used in this analysis was scraped from [Basketball Reference](https://www.basketball-reference.com/playoffs/series.html) using my Python script containing the BS4, request, and pandas modules. Some simple calculations were done on the play by play tables to track the largest lead of each game and the largest comeback. The data was stored as tuples in Pandas DataFrames where the first value is the lead or comeback and the second value is an abbreviation for the date and location the game took place *199905080ATL* for example, is the game on May 8th, 1999 in Atalanta.

## Tools and Libraries

- Python (pandas, numpy, matplotlib)
- Jupyter Notebook 

## File Structure
Outline the structure of your project files and folders. For example:

## Analysis Process
Explain the general steps of your analysis:
1. Data cleaning and preprocessing
2. Exploratory Data Analysis (EDA)
3. Data visualization
4. Statistical analysis or modeling
5. Results interpretation

## Results
Summarize the key findings from your analysis. Include any visuals or links to relevant documents.

## How to Run
Provide instructions on how to set up and run the project:
