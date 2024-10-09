# 6.16:  Continuing the Name class, set a class variable 'label' that refers to a string 'Name: ' --
# this will serve as the label to be printed along with a person's name

import runreport

n = Name('David', 'Blaikie')

print(n.get_name())             # Name:  David Blaikie
print(n.get_rname())            # Name:  Blaikie, David


n2 = Name('Marie', 'Sanchez')

print(n2.get_name())            # Name:  Marie Sanchez
print(n2.get_rname())           # Name:  Sanchez, Marie

