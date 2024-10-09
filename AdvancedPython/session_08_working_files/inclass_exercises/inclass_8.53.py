# 8.53:  MultiIndex:  slicing at top level.  Slice the multi-index to show just 'Account' and
# 'Quantity', and just for Manager 'Debra Henley'.

import pandas as pd
import numpy as np

df = pd.read_excel("../sales-funnel.xlsx")

table = pd.pivot_table(df, index=['Manager', 'SalesRep'],
                           aggfunc='sum')

table.loc['Debra Henley', ['Account', 'Quantity']]

