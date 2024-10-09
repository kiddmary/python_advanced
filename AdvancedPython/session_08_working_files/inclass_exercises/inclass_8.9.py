# 8.9:  Exclude header and footer; set index.  Add keyword arguments to configure the pd.read_csv()
# function.

# The revenue_extended.csv file has 2 header lines (use skiprows=) and 2 footer lines (use
# skipfooter=).  The column we'd like to use as the index is the 'id' column (use index_col=).
# 
# Skipping rows means we must use the 'python' engine -- configure with engine=

import pandas as pd

fname = '../revenue_extended.csv'  # has extra headers, id field

df = pd.read_csv(fname)





