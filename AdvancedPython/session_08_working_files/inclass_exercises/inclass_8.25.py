# 8.25:  Vectorizing with function.  Use .apply[] with a condition to create column 'revf'
# converting 'revenue' to a string with formatting.

def format(n):
    return f'${n:,.2f}'   # makes 2.3 into '$2.30'


import pandas as pd

df = pd.read_csv('../revenue.csv')



df

