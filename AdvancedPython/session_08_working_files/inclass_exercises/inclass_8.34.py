# 8.34:  Reorder the columns on the DataFrame to 'float', 'num', and 'terxt' (deliberately misspell
# 'text') using .reindex().  Note that the 'terxt' column springs into existence with empty values.

import pandas as pd

data = [
    [1, 2.5, 'apple'],
    [2, 3.0, 'banana'],
    [3, 4.2, 'orange']
]

df = pd.DataFrame(data, columns=['num', 'float', 'text'],
                        index=['c', 'b', 'a'])




df

