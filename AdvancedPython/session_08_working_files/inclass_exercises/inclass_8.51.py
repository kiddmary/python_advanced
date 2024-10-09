# 8.51:  pd.pivot_table():  dual-column aggregation.  Perform the same pivot as previous, but group
# by by both 'SalesRep' and 'Product'.

import pandas as pd
import numpy as np

df = pd.read_excel("../sales-funnel.xlsx")

dfpt = pd.pivot_table(df, index=['SalesRep', 'Product'],
                          aggfunc='sum')

dfpt

