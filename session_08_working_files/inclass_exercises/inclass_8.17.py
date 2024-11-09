# 8.17:  Slice based on dual condition.  Select for a 'high' of > 90 and a 'precip' of > 0.5.
# Separate the tests with an & and put parentheses around each.  (This will uncover an anomaly that
# we'll solve next.)

import pandas as pd

fname = '../weather_newyork_narrow.csv'

df = pd.read_csv(fname)

hitemps = df.loc[ (df.high > 90) & (df.precip > 0.5) ]

hitemps

