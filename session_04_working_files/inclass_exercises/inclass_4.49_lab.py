# 4.49:  Match on each string that ends in .jpg or .JPG

import runreport
import re

match_strings = [
    'hello world 00',
    'goodbye world    ',
    ' 23 bonjour',
    'wilkommen23  ',
    'aloha',
    '99',
    '00',
    '88557799',
    'Que 3 Tal!',
    'myfile.jpg',
    'yourfile.JPG'
]

count = 0
for string in match_strings:
    if re.search(r'\.jpg$', string, re.I):
        print(string)
        count += 1
print(f'count:  {count}')

# Expected Output:
# myfile.jpg
# yourfile.JPG
# count: 2