# 7.2:  Without calling any of the below attributes, print the type of each.

import json
import sys

mylist = [1, 2, 3, 4]
mystr = 'hello'
fh = open('../pconfig.json')

# print the type of each of the following:

# mylist.append
print(type(mylist.append))

# mystr.upper
print(type(mystr.upper))

# json.load
print(type(json.load))

# sys.argv
print(type(sys.argv))