"""
 select_rows.py -- write specific rows containing a specific statement acronym value

 Author: Mary Kidd (marykidd@nypl.org)
 Last Revised: 10/11/2024
"""

import argparse
import os
import sys
import csv

parser = argparse.ArgumentParser(prog=os.path.basename(sys.argv[0]))

parser.add_argument('-s', '--source', required=True)
parser.add_argument('-t', '--target', required=True)
parser.add_argument('-c', '--column', required=True)
parser.add_argument('-v', '--value', required=True)

args = parser.parse_args()

file_src_name = sys.argv[2]
file_trg_name = sys.argv[4]
column_name = sys.argv[6]
column_val = sys.argv[8]

fh = open(file_src_name, 'r')
reader = csv.reader(fh)
headers = next(reader)

wfh = open(file_trg_name, 'w', newline='')
writer = csv.writer(wfh)

writer.writerow([headers[0], headers[1], headers[2]])

for row in reader:
    if row[1] == 'NY':
        writer.writerow(row)

