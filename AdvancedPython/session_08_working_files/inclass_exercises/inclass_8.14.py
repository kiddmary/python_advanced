# 8.14:  Use .loc[] to slice columns and rows.  Select all rows but just the 'company' and 'revenue'
# columns (use ':' for the row selector).

import pandas as pd

fname = '../revenue_extended.csv'

df = pd.read_csv(fname, skiprows=2,
                        skipfooter=2,
                        index_col='id',
                        engine='python')



df

