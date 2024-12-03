# 7.5:  Use hasattr() in an if statement to check for an attribute within an object;
# if True, use getattr() to retrieve and print the attribute.

import sys                           # retrieve the 'version' attribute

mylist = ['a', 'b', 'c']             # retrieve the 'append' attribute

for attr in dir(sys):
    print(attr)

attr = [attr for attr in dir(sys) if 'frame' in attr]
print(attr)
