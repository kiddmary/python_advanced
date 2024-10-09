# 8.6:  See the head and tail of a DataFrame:

#   * Use .head() and .tail()
#   * Use .columns and .index
# 

import pandas as pd

fname = '../weather_newyork_narrow.csv'

df = pd.read_csv(fname)



df

