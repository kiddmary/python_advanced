# 1.13:  Use csv.DictReader to read the header line of a file.

# Continue the previous solution -- read and print the file's headers using the .fieldnames
# attribute.

import csv

fname = '../revenue.csv'

fh = open(fname)

dreader = csv.DictReader(fh)



# Expected Output:

# ['company', 'state', 'price']

