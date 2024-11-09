# 8.35:  Use .set_index() to set the id column for the DataFrame as the index.

# Next, use .reset_index() to reset the index to the default (integers), while moving the index to a
# new column.  Lastly, add the drop=True parameter argument to drop the index entirely, and note
# that the old index has been dropped.

import pandas as pd

fname = '../revenue_extended.csv'

df = pd.read_csv(fname, skiprows=2,
                        skipfooter=2,
                        engine='python')



df

