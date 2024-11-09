# 8.23:  Vectorizing with condition.  Continuing the above solution, use .loc[] with a condition to
# set 'tax' to 0.0625 for all 'NJ' rows, then recalculate tax amount.

import pandas as pd

df = pd.read_csv('../revenue.csv')

df['tax'] = 0.04

# your code here

df['tax amt'] = df.revenue * df.tax

df

