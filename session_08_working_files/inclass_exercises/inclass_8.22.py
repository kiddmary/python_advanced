# 8.22:  Vectorize column value.  Add a new column 'tax amt', set to the 'revenue' value * 'tax'
# amount.

import pandas as pd

df = pd.read_csv('../revenue.csv')

df['tax'] = 0.04



df

