import pandas as pd
import numpy as np

comebacks = pd.read_csv('playoffComebacks.csv')
leads = pd.read_csv('playoffLeads.csv')

keys = range(1997, 2024)

comeback_avg = comebacks.mean()
comeback_avg.head()