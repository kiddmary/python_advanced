# 5.2:  Write a function greet() with one positional argument (a first name) and one
# keyword argument (an optional last name).  Make the default for last= the value
# None.  Call as shown.

def greet(first, last=None):
    if not last:
        return f'Hi, {first}!'
    else:
        return f'Hi, {first} {last}!'

x = greet('Joe')
print(x)                 # Hi, Joe!

y = greet('Joe', 'Wilson')
print(y)                 # Hi, Joe Wilson!