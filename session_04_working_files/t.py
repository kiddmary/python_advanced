
"""
solution_4.1.py
Author: Louisa Shriver (lafshriver@gmail.com)
Last Revised: 4/25/2023
"""

import re

fh = open('access_log.txt')                # 'file' object
count = 0                                  # int, 0
counting_dict = {}                         # dict, {}

for line in fh:

    usermatch = re.search(r'(/~)([a-z]+[0-9]+)/', line)       # 're.Match' object
    usermatch2 = re.search(r'(/~)([a-z]+[0-9]+)', line)
    if not usermatch and usermatch2 and bytematch:
         print(line)
         count += 1
         continue

    bytematch = re.search(r'\d+$', line)
    if not usermatch or not bytematch:
        continue

    user = usermatch.group(2)                              # str, 'cmk380'
    byte = bytematch.group(0)                              # str, '30'

    if user not in counting_dict:
        counting_dict[user] = 0

    counting_dict[user] = counting_dict[user] + int(byte)
    count += 1

print(f' {count} matched found (both user id and end-of-line bytes found on the line)')

for key in sorted(counting_dict, key=counting_dict.get, reverse=True):
    if counting_dict[key] < 10000000:
        continue
    else:
        print(f'{key}: {counting_dict[key]}')



# Hi David, I have made the changes in the printed text of the count and the grouping so it should all look good now!
# It turns out it was the slash at the end was what was causing us to get different results! So there must be some ID's that do not have a slash following them

