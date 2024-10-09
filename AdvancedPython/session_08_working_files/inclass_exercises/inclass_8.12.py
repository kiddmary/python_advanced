# 8.12:  Slice rows using .loc[] and a list of labels.  Select just 'hd34', 'hp21' and 'tc77'.

import pandas as pd

fname = '../revenue_extended.csv'

df = pd.read_csv(fname, skiprows=2,
                        skipfooter=2,
                        index_col='id',
                        engine='python')



df

