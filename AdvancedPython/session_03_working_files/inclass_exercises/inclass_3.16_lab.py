# 3.16:  Read and parse JSON data.

# Continue the previous program by using the .json() method of the response object to read the data
# as a JSON object.
# 
# You should find that the object is a dict, that it has one key list with a value that is a list,
# and that if you loop through this list of dicts, the key author is the author's name, and
# definition is the definition.

import runreport
import requests

url = 'http://api.urbandictionary.com/v0/define'

params = {'term': 'sigma'}

response = requests.get(url, params=params)

json_obj = response.json()
print(json_obj)

for defs in json_obj['list']:
    print('=====')
    print('')
    print(f'Author: {defs['author']}')
    print('')
    print(f'Definition: {defs['definition']}')
    print('')