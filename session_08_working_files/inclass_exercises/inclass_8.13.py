# 8.13:  Slice rows using .loc[] and a range of labels.  Select 'ts06' through 'df8'.

import pandas as pd

fname = '../revenue_extended.csv'

df = pd.read_csv(fname, skiprows=2,
                        skipfooter=2,
                        index_col='id',
                        engine='python')



df

