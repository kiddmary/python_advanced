# 8.24:  .replace() method.  Returning to the 'precip' column, replace the non-numeric value we
# identified previously with 0.  Use vectorized condition as in previous, or the Series .replace()
# method.

import pandas as pd

df = pd.read_csv('../weather_newyork_narrow.csv')



df

# After replacing the value, run .unique() to see that the anomalous value is no longer there.
# 
# Next, bring this solution to the exercise that failed and try again...
# 
# ...still no joy?  Wait until we can manipulate dtypes -- coming up.

