"""
 select_rows.py -- write specific rows for a specific column and matching row value

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

file_src_name = args.source
file_trg_name = args.target
column_name = args.column
column_val = args.value

fh = open(file_src_name, 'r')
reader = csv.reader(fh)
headers = next(reader)

wfh = open(file_trg_name, 'w', newline='')
writer = csv.writer(wfh)

idx = headers.index(column_name)
writer.writerow(headers)

for row in reader:
    if row[idx] == column_val:
        writer.writerow(row)

fh.close()
wfh.close()