# 4.12:  Inverse Custom Character Class.
# Match on each string that has any character that is not a letter.

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
    if re.search(r'[^A-Za-z]', string):
        print(string)
        count += 1
print(f'count:  {count}')

# Expected Output:
# hello world 00
# goodbye world
#  23 bonjour
# wilkommen23
# 99
# 00
# 88557799
# Que 3 Tal!
# myfile.jpg
# yourfile.JPG
# count: 10