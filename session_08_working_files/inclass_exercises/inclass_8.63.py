# 8.63:  Converting a DataFrame column/index to Timestamp.  View the below dataframe and note the
# date column EST.  Use pd.to_datetime() or .astype() method to convert the 'EST' series to
# 'datetime64[ns]', then use .set_index() with the column name and drop=True to set the column as
# the index.  Check the dtype of the index.

import pandas as pd

df = pd.read_csv('../weather_newyork.csv')



df

# If your dtype shows as '<M8[ns]' it means that the date is 'timezone-aware'; if it shows as
# 'datetime64[ns]' it signifies 'timezone-naive' (meaning it is not aware of any timezone).  Since
# timezone-aware timestamps know their timezone, they can be compared with other timezone-aware
# dates to do calculations and comparisons between timestamps.

