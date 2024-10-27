# 3.8:  View response headers.

# Continuing the previous exercise, use the .headers attribute to retrieve the headers coming back
# as a dict from the response.  Loop through and print each key/value pair in the dict.

import requests
import runreport

url = 'https://pycoders.com'

response = requests.get(url)

text = response.text
print(f'Status code: {response.status_code}')

headers = response.headers

for key, value in headers.items():
    print(f'{key}: {value}')

wfh = open('pycoders.html', 'w')
wfh.write(text)
wfh.close()