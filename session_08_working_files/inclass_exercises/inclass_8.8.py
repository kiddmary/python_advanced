# 8.8:  View selected rows by index.  Use .iloc[] with a numeric slice to see the 50th through 53rd
# rows from this large DataFrame.

import pandas as pd

fname = '../weather_newyork_narrow.csv'

df = pd.read_csv(fname)



df

