# 6.10:  Create a "getter" method.
# Create a method get_value() that returns the .value attribute from the instance.

class Say:
    def __init__(self, val):
        self.thisval = val

    def get_value(self):
        return self.thisval

obj = Say(100)

vl = obj.get_value()
print(vl)                # 100

# Expected Output:
# 100