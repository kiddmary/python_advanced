# 8.31:  Print the .index and .columns attributes on this DataFrame.  Then reorder the rows to 'a',
# 'b', 'c'

import pandas as pd


data = [
    [1, 2.5, 'apple'],
    [2, 3.0, 'banana'],
    [3, 4.2, 'orange']
]

df = pd.DataFrame(data, columns=['num', 'float', 'text'],
                        index=['c', 'b', 'a'])




df

