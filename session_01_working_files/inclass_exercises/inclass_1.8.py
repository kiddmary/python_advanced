# 1.8:  Write individual rows to a CSV file using csv.writer.  Take the following steps,
#       testing as you go:

#   1. Open a file for writing and pass the filehandle to csv.writer() (when opening the
#      file for writing, include the newline='' argument to open() so newlines will be
#      written properly).
#   2. Use .writerow() on the writer object to write each list to the file, starting with
#      the header list.
#   3. Close the file, then open and view newfile.csv in the session directory.

import csv

header = ['name', 'address', 'state', 'zip']

row1 = ['Joe', '123 Main', 'CA', '91603']
row2 = ['Marie', '234 Camarino', 'NJ', '92325']

fname = '../newfile.csv'     # a new file, or replacing old if exists

wfh = open(fname, 'w', newline='')
writer = csv.writer(wfh)
writer.writerow(header)
writer.writerow(row1)
writer.writerow(row2)

wfh.close()