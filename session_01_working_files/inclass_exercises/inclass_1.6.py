# 1.6:  Use csv.reader to read a file.  Take the following steps, testing as you go:

#   1. Open a file and pass the file object to csv.reader()
#   2. Loop through the reader object line by line, printing each line.
#      Note the type of the object representing each row.
#   3. Subscript the float value from each list and convert to float.
#   4. Initialize a float variable 0.0 at the top and add each float value to it inside the
#      loop, producing a sum.

import csv

filename = '../revenue.csv'

fh = open(filename)
reader = csv.reader(fh)
headers = next(reader)

float_adder = 0.0

for rows in reader:
    row_val = rows[-1]
    float_val = float(row_val)
    float_adder = float_adder + float_val

sum = round(float_adder,2)
print(sum)