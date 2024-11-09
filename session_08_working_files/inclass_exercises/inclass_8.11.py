# 8.11:  View Series .name and .index.

import pandas as pd

fname = '../revenue_extended.csv'  # has extra headers, id field

df = pd.read_csv(fname, skiprows=2,
                        skipfooter=2,
                        index_col='id',
                        engine='python')

s = df.company



s

