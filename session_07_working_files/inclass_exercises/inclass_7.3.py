# 7.3:  What exception does this code cause Python to raise and why?

mystr = '1, 2, 3, 4, 5'

mystr.append(5)

# Attribute Error: The 'str' object has no attribute 'append'
# (this is specific to the list object)