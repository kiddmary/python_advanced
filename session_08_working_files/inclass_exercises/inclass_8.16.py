# 8.16:  Slice based on single condition.  Using .loc[] with a condition, look for all 'high' temps
# above 100, then try above 90.

import pandas as pd

fname = '../weather_newyork_narrow.csv'

df = pd.read_csv(fname)



df

# Then, add 2nd 'bucket' to .loc[] to select the 'high' an d 'precip' columns.

