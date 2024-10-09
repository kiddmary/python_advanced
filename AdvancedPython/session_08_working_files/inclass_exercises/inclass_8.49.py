# 8.49:  pd.pivot_table():  single-column aggregation.  First, view the DataFrame above.  Slice the
# DataFrame for just the 'SalesRep' and 'SaleAmount' columns.  Then use pd.pivot_table(df) to
# aggregate by 'SalesRep', using the index= parameter.

import pandas as pd

df = pd.read_excel("../sales-funnel.xlsx")

dfpt = pd.pivot_table(df[['SalesRep', 'SaleAmount']], index='SalesRep')

dfpt

# The default summary method is average (i.e., .mean())

