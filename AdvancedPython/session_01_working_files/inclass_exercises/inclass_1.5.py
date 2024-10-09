# 1.5:  Add an argument allowing multiple values.

# Continue the same program; add argument --cities and add the nargs='+' argument to allow
# multiple values.
# 
# Call the program with the --cities argument and a couple of city values.

import argparse
import os
import sys

parser = argparse.ArgumentParser(
                    prog=os.path.basename(sys.argv[0]),
                    description='prints your name!')

parser.add_argument('-n', '--name', required=True)
parser.add_argument('-c', '--color', choices=['red', 'blue', 'green'])
parser.add_argument('-t', '--cities', nargs='+')

args = parser.parse_args()

print(args.name)
print(args.color)
print(args.cities)

# Sample program run:
# % python inclass_ex.py --name David --color red --cities Chicago 'New York'
# David
# red
# ['Chicago', 'New York']
# %