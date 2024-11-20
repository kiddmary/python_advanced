# 6.9:  Set an instance attribute in __init__().

# Create a method __init__(self, num) that sets numin self as a .value attribute.
# At bottom, print obj.value to see the value.

class Live:
    """ a class that just wants to live """
    def __init__(self, num):
        self.value = num

obj = Live(5)
print(obj.value)

# Expected Output:
# 5