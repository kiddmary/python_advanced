# 1.14:  Use csv.DictWriter to write a header to a file.

# Starting with the following filename and headers list, open the file for writing, then instantiate
# a csv.DictWriter object with the file object and headers; use the .writeheader() argument to write
# the header row.
# 
# Make sure to close the write filehandle with .close() (make sure to include the parentheses!)
# after all writing is done.
# 
# Run the program, then check the file to see that it has been created and contains the headers

import csv

filename = '../newfile.csv'

wfh = open(filename, 'w', newline='')

headers = ['fname', 'lname', 'state']

dwrite = csv.DictWriter(wfh, headers)

dwrite.writeheader()

wfh.close()

# After running, the file newfile.csv in the parent directory should have the following text:
# fname,lname,state