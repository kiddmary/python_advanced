# 1.7:  Use csv.reader to read the header of a file.  Using the code solution from the
# previous exercise, before the for block, use a call to next(reader) to retrieve and
# print the header of the file, noting that the loop then begins on the next line of the file.

import csv

fh = open('../revenue.csv')        # 'file' object

reader = csv.reader(fh)            # csv.reader object

fsum = 0.0                         # float, 0.0

header = next(reader)
print(header)

for row in reader:                 # list, ["Haddad's", 'PA', '239.5']
    fval = float(row[-1])          # float, 239.5
    fsum = fsum + fval             # float, 239.5

print(fsum)