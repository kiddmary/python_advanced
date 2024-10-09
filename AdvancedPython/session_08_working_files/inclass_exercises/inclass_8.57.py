# 8.57:  MultiIndex:  First review the below DataFrame; then use .query('Status in ["pending",
# "won"]') to select rows.

import pandas as pd

df = pd.read_excel("../sales-funnel.xlsx")

dfq = df.query('Status in ["pending", "won"]')

dfq

