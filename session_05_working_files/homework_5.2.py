"""
 homework_5.2.py -- Read, sort by YYYYMMDD and write to file

 Author: Mary Kidd (kiddmary@gmail.com)
 Last Revised: 11/12/2024
"""

file_to_sort = open('dated_file.csv')
lines = file_to_sort.readlines()

def getyear(sorterdate):
    column = sorterdate.split(',')
    date = column[0]
    month, day, year = date.split('/')
    combined = year + month + day

    return combined

sortedlines = sorted(lines, key=getyear)

file_to_write = 'sorted_file.csv'

wfh = open(file_to_write, 'w')

for line in sortedlines:
    wfh.write(line)
wfh.close()

print(f'wrote to {file_to_write}')