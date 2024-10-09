# 3.10:  Demo exercise:  issue a request and view elements of the request.

# First, issue the following request and view the headers reflected back.
# 
# Next, uncomment the 'headers' lines to see how http_reflect "sees" you (i.e., what browser and
# platform it thinks you are requesting from).
# 
# Finally, change 'text/plain' to 'text/html' and see http_reflect respond with HTML instead of
# plain text.

import requests

spoof_browser = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"

response = requests.get('http://davidbpython.com/cgi-bin/http_reflect'
                        #, headers={
                        #         'User-Agent':  spoof_browser,
                        #         'Accept':      'text/plain',
                        #         }
                        )

print(response.text)

