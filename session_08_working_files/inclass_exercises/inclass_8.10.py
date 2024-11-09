# 8.10:  View the 'company' column using subscript syntax (df['company']), and the same column using
# attribute syntax (df.company).  Print the type of this object.

import pandas as pd

fname = '../revenue_extended.csv'  # has extra headers, id field

df = pd.read_csv(fname, skiprows=2,
                        skipfooter=2,
                        index_col='id',
                        engine='python')



df

