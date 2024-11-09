# 8.55:  MultiIndex:  "cross section" slicing.  Use the .xs() method with level=1 to show rows just
# for 'Craig Booker'.

import pandas as pd
import numpy as np

df = pd.read_excel("../sales-funnel.xlsx")

table = pd.pivot_table(df, index=['Manager', 'SalesRep'],
                           aggfunc='sum')

txs = table.xs('Craig Booker', level=1)

txs

