# 6.1:  Define a class.

# Use the class statement with name MyClass (or you may substitute a name of your own choice).
# To fill the otherwise empty block, use the pass statement.
# 
# Initialize an instance of the class and print its type to show that it is an instance of
# the class.

# Expected Output:
# <class '__main__.MyClass'>

class Counter:
    def __init__(self):
        print('instance being created!')
    def hello(self, name):
        print(f"I'm {name}!")

c = Counter()
c2 = Counter()

c.hello('Mary')
c2.hello('Flower')