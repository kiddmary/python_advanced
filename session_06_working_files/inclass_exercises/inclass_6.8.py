# 6.8:  Create an __init__() method.

# Add a method to the below class, __init__(self) that inside the function announces and
# prints the argument self, i.e. print(f'self:    {self}').
# 
# Construct 2 new instances, and then print each instance.
# Put a blank line between each instance.

class Be:
    def __init__(self):
        print(f'self: {self}')

obj1 = Be()
print(f'object:  {obj1}')

print()

obj2 = Be()
print(f'object:  {obj2}')

# Expected Output:

# self:    <__main__.Be object at 0x10d648250>
# object:  <__main__.Be object at 0x10d648250>
# 
# object:  <__main__.Be object at 0x10d648a50>
# self:    <__main__.Be object at 0x10d648a50>

# (Note that the above 0x hex codes will not be the same as mine, but the values in each pair should
# match.)