# 8.43:  Using the joined student tables, check to see if any null values can be found in the
# 'course' column.

import pandas as pd

sgrades = pd.read_csv('../student_db_grades.csv', sep=':')
snames = pd.read_csv('../student_db_names.csv')

sj = pd.merge(sgrades, snames, on='id', how='outer')

sj


# see boolean column of whether missing or not - use .isnull()


# see whether there are any missing values - use any() with .isnull()


# select rows with missing data - use .isnull() as a condition to .loc[]



