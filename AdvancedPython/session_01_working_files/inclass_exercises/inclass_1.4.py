# 1.4:  Add an argument restricted to specific choices.

# Continue the same program; add an argument 'color' with the choices= argument.  Restrict the
# choices to blue, green or red.
# 
# Print the value of the color argument.
# 
# Call the program with a --color argument and one of the valid colors; then call the program with
# --color and an invalid choice; note that it is rejected.

import argparse
import os
import sys

parser = argparse.ArgumentParser(
                    prog=os.path.basename(sys.argv[0]),
                    description='prints your name!')


parser.add_argument('-n', '--name', required=True)

args = parser.parse_args()

print(args.name)

# Sample program run:

# % python inclass_ex.py --name David --color red
# David
# red
# % python inclass_ex.py --name David --color purple
# usage: inclass_ex.py [-h] -n NAME [-c {red,blue,green}]
# inclass_ex.py: error: argument -c/--color: invalid choice: 'purple' (choose from 'red', 'blue', 'green')
# %

