# 7.1:  Identify the object and attribute in each of the bottom 4 code lines.

import json
import sys

mylist = [1, 2, 3, 4]
mystr = 'hello'
fh = open('../pconfig.json')

# identify the object and attribute in each of the below
mylist.append(5)    # object: mylist (list)  | attribute: append (method)
mystr.upper()       # object: mystr (string) | attribute: upper (method)
json.load(fh)       # object: json (module)  | attribute: load (function)
sys.argv            # object: sys (module)   | attribute: argv (function)