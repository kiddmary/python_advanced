# 5.17:  Sort the lines of revenue.csv by the numeric value in the last field by passing
# the list of lines returned from readlines() of the file to sorted() and using a custom
# sort sub similar to an earlier exercise.  (I am also rstrip()ping each line before
# printing it.)

def sortnum(line):
    words = line.split(',')
    return float(words[-1])

fh = open('../revenue.csv')
lines = fh.readlines()

for line in sorted(lines, key=sortnum):
    print(line)

# Expected Output:
# Dothraki Fashions,NY,5.98
# Hipster's,NY,11.98
# Awful's,PA,23.95
# Westfield,NJ,53.90
# The Clothiers,NY,115.20
# The Store,NJ,211.50
# Haddad's,PA,239.50