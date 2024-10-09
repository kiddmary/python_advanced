# 8.33:  Using .rename(), rename column labels: 'EST' -> 'date', 'Max TemperatureF' -> 'max_temp'
# and 'Min TemperatureF' -> 'min_temp'.

import pandas as pd

df = pd.read_csv('../weather_newyork.csv')

dfs = df.reindex(['EST', 'Max TemperatureF', 'Min TemperatureF'], axis=1)



dfs

