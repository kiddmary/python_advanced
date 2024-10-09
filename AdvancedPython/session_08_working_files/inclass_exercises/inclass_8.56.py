# 8.56:  MultiIndex:  use .query('Manager == "Debra Henley"') to select rows.

import pandas as pd
import numpy as np

df = pd.read_excel("../sales-funnel.xlsx")

table = pd.pivot_table(df, index=['Manager', 'SalesRep'],
                           aggfunc='sum')

table.query("Manager == 'Debra Henley'")

# table.query("Manager == 'Debra Henley' and SalesRep == 'Craig Booker'")

# table.query("SalesRep in ['Craig Booker', 'Daniel Hilton']")

