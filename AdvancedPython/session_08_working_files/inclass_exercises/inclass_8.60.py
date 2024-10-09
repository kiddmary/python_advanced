# 8.60:  Create a pd.Timedelta interval object for one day (use the days=1 argument).  Add it to the
# Timestamp object to produce a new Timestamp object with the advanced date.  Print the object to
# see the new date.

import pandas as pd

ts = pd.Timestamp('3/3/2020')

td = pd.Timedelta()

ts2 = ts + td
print(ts2)

