# 6.15:  Continuing the Name class, add a method .get_name() that returns the full name as
# 'first name last name'.
# Finally, add another method .get_rname() that returns the name in reverse order (last, first).

# import runreport

class Name:
    def __init__(self, fname, lname):
        self.first = fname
        self.last = lname

    def get_name(self):
        return f'{self.first} {self.last}'

    def get_rname(self):
        return f'{self.last} {self.first}'

n = Name('David', 'Blaikie')

print(n.get_name())             # David Blaikie
print(n.get_rname())            # Blaikie, David