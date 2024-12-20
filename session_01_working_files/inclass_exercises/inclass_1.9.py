# 1.9:  Write multiple rows to a CSV file using csv.writer.  Follow the same steps as above,
#       but use .writerows() to write the entire list of lists to the file.  Close the file,
#       then look for newfile2.csv in the session directory.

import csv

rows = [
         [ 'date', 'temp', 'wind' ],
         [ '2020-06-13', '78.3', '6' ],
         [ '2020-06-14', '77.0', '8' ],
       ]

fname = '../newfile2.csv'

wfh = open(fname, 'w', newline='')

writer = csv.writer(wfh)

writer.writerow(rows)

wfh.close()