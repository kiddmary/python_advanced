# 8.50:  pd.pivot_table() specifying a summary function.  Perform the same pivot as previous, but
# use the aggfunc= parameter to specify a sum (use 'sum').

import pandas as pd
import numpy as np

df = pd.read_excel("../sales-funnel.xlsx")

dfpt = pd.pivot_table(df, index='SalesRep',
                          aggfunc='sum')

dfpt

