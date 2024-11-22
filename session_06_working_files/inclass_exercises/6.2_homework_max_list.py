"""
 6.2_homework_max_list.py -- Append set amount of values to a list

 Author: Mary Kidd (kiddmary@gmail.com)
 Last Revised: 11/19/2024
"""
class MaxSizeList:
    def __init__(self, maxlist):
        self.mylist = []
        self.maxsize = maxlist
    def push(self, newval):
        self.mylist.append(newval)
        if len(self.mylist) > self.maxsize:
            self.mylist.pop(0)

    def get_list(self):
        return self.mylist

a = MaxSizeList(3)
b = MaxSizeList(1)

a.push("hey")
a.push("ho")
a.push("let's")
a.push("go")

b.push("hey")
b.push("ho")
b.push("let's")
b.push("go")

print(a.get_list())     # ['ho', "let's", 'go']
print(b.get_list())     # ['go']