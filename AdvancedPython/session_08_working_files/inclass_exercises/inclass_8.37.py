# 8.37:  Use .sort_values() to sort the DataFrame by the 'high' value.  Use ascending=False to
# reverse the sort.

import pandas as pd

fname = '../weather_newyork_narrow.csv'

df = pd.read_csv(fname, index_col='date')



df

