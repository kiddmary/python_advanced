# 8.41:  View the two below DataFrames.  Then use pd.merge() to join the student_db_grades.csv and
# student_db_names.csv files into a single DataFrame, joining on the id (use on='id').  Compare
# "how='outer'" (19 rows, including missing data at the end) to "how='inner'" (only 15 rows, with
# ids common to both tables) to effect an outer join.

import pandas as pd

sgrades = pd.read_csv('../student_db_grades.csv', sep=':')
snames = pd.read_csv('../student_db_names.csv')

sgrades.head(2)
print('===')
snames.head(2)
print('===')




