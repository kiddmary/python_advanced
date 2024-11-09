# 1.16:  Create a dictionary by zipping up two lists.

# Given the following list of headers and data row, use dict(zip()) with the two lists to zip the
# two lists together into a list of 2-item tuples, and convert them to a dict.  Print the dict.

headers = ['fname', 'lname', 'state']

data = ['Joe', 'Wilson', 'CA']

d = dict(zip(headers, data))

print(d)
# Expected Output:

# {'fname': 'Joe', 'lname': 'Wilson', 'state': 'CA'}

