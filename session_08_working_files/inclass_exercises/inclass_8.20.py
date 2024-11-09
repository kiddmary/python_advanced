# 8.20:  Reverse a test.  Use ~ (the tilde character) to reverse the above test so that we show only
# rows that are NOT 'NY' or 'NJ'.

import pandas as pd

df = pd.read_csv('../revenue.csv')

df2 = df.loc[ df.state.isin(['NY', 'NJ']) ]

df2

