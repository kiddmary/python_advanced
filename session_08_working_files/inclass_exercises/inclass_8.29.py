# 8.29:  Set the dtype for a column.  First, use .dtypes to show the column types; then replace the
# '-' values in the 'transactions' column with 0's.  Finally, set the column dtype to 'int'.

import pandas as pd

df = pd.read_csv('../revenue_extended.csv', skiprows=2,
                                            skipfooter=2,
                                            engine='python')

df.dtypes



df

