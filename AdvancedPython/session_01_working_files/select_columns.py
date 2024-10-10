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
print(headers)

for row in reader:
    print(row)

fh.close()

wfh = open(file_trg_name, 'w', newline='')
writer = csv.writer(wfh)
writer.writerow([headers[0]])


