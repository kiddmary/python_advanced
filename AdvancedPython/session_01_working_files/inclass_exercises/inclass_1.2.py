# 1.2:  Use argparse to accept a required argument from the command line.

# Starting with the below code, use parser.add_argument() to add argument 'name'.
# The argument should expect either -n or --name as identifier at the command line.
# Include a required=True argument to make the argument required.
# 
# Call .parse_args() on the parser object.  The program should then print the value of the 'name' argument.
# 
# Test the program by running it from a Terminal or Command Prompt.
# 
# Then, test it a second time by omitting the argument, and note that the required=True
# causes the program to output an error message.

import argparse
import os
import sys

parser = argparse.ArgumentParser(
                    prog=os.path.basename(sys.argv[0]))

parser.add_argument('-n', '--name', required=True)
args = parser.parse_args()
print(args.name)

# Sample Run (note that the '%' represents your command prompt - yours will look different).

# % python inclass_ex.py --name David
# David
# %  python inclass_ex.py
# usage: inclass_ex.py [-h] -n NAME
# inclass_ex.py: error: the following arguments are required: -n/--name