# 6.3:  Add argument and return value to method.
# Add the method doubleit() below, that doubles the value passed to it.
class Numbers:
    def doubleit(self, myval):
        return myval * 2

num = Numbers()
val = num.doubleit(5)
print(val)               # 10

val2 = num.doubleit(100)
print(val2)              # 200

# Expected Output:
# 10
# 200