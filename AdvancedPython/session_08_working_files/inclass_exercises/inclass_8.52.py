# 8.52:  pd.pivot_table():  further agg by secondary value.  Perform the above pivot on just
# 'SalesRep', but use columns= with a list to show the results broken down by 'Product'.

import pandas as pd
import numpy as np

df = pd.read_excel("../sales-funnel.xlsx")

dfpt = pd.pivot_table(df, index='SalesRep',
                          aggfunc='sum',
                          values=['SaleAmount', 'Quantity'],
                          columns='Product')

dfpt

