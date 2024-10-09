# 1.12:  Use csv.DictReader to read a file line-by-line, each line a dict.

# As you loop through the DictReader object, print each row dict.

import csv

fname = '../revenue.csv'

fh = open(fname)

dreader = csv.DictReader(fh)

for row in dreader:
	print(row)

# Expected Output:

# {'company': "Haddad's, Inc.", 'state': 'PA', 'price': '239.5'}
# {'company': 'Westfield', 'state': 'NJ', 'price': '53.9'}
# {'company': 'The Store', 'state': 'NJ', 'price': '211.5'}
# {'company': "Hipster's", 'state': 'NY', 'price': '11.98'}
# {'company': 'Dothraki Fashions', 'state': 'NY', 'price': '5.98'}
# {'company': "Awful's", 'state': 'PA', 'price': '23.95'}
# {'company': 'The Clothiers', 'state': 'NY', 'price': '115.2'}

