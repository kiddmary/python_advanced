import argparse
import os
import sys
import csv

parser = argparse.ArgumentParser(prog=os.path.basename(sys.argv[0]))

parser.add_argument('-s', '--source', required=True)
parser.add_argument('-t', '--target', required=True)

args = parser.parse_args()

file_src_name = sys.argv[2]
file_trg_name = sys.argv[4]

fh = open(file_src_name, 'r')
reader = csv.reader(fh)
headers = next(reader)

wfh = open(file_trg_name, 'w', newline='')
writer = csv.writer(wfh)

writer.writerow([headers[0], headers[1], headers[17], headers[19]])

for row in reader:
    sel_fields = [ row[0], row[1], row[17], row[19]]
    writer.writerow(sel_fields)

fh.close()
wfh.close()




