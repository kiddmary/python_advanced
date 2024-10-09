# 1.15:  Use csv.DictWriter to write lines to a file.

# Continuing from the previous solution (below, with some data line dictionaries added), use
# .writerow() to write the dicts to the file.

import csv

filename = 'newfile.csv'

headers = ['fname', 'lname', 'state']

data_lines = [
               { 'fname': 'Joe', 'lname': 'Wilson', 'state': 'CA' },
               { 'fname': 'Mike', 'lname': 'Sanchez', 'state': 'NY' },
               { 'fname': 'Marie', 'lname': 'Obubwe', 'state': 'NJ' },
             ]

wfh = open(filename, 'w')

dwriter = csv.DictWriter(wfh, headers)

dwriter.writeheader()

wfh.close()


# After running, the file newfile.csv in the parent directory should have the following text:

# fname,lname,state
# Joe,Wilson,CA
# Mike,Sanchez,NY
# Marie,Obubwe,NJ

