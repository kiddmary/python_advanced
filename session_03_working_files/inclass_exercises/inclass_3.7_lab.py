# 3.7:  View response status code.

# Continuing the previous exercise, use the .status_code attribute to view the response status.  Now
# change the URL to something you wouldn't expect to be correct, run and view the status code.

import runreport
import requests

url = 'https://pycoders.com/'

response = requests.get(url)

text = response.text
print(f'Status code: {response.status_code}')

wfh = open('pycoders.html', 'w')
wfh.write(text)
wfh.close()