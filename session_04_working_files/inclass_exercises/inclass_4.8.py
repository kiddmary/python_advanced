# 4.8:  "Not a digit" character class.
# Match on each string that has a character that is not a digit.

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
    if re.search(r'\D', string):
        print(string)
        count += 1
print(f'count:  {count}')

# Expected Output:
# hello world 00
# goodbye world
#  23 bonjour
# wilkommen23
# aloha
# Que 3 Tal!
# myfile.jpg
# yourfile.JPG
# count: 8