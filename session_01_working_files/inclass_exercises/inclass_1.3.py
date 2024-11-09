# 1.3:  View the help message.  Starting with the above solution, add a description=
# argument to ArgumentParser; the value should be a string explaining what the program does.

# Call the same program with the --help or -h flag.  Note the automated output explaining
# how the program works.

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

# % python inclass_ex.py --help
# usage: inclass_ex.py [-h] -n NAME
# 
# prints your name!
# 
# options:
#   -h, --help            show this help message and exit
#   -n NAME, --name NAME