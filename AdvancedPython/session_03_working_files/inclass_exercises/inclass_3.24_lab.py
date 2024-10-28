# 3.24:  Scrape and print the <h3> tag in the middle of the page (not the first <h3> tag)

import runreport
from bs4 import BeautifulSoup

fname = '../test_scrape.html'

fh = open(fname)
text = fh.read()

soup = BeautifulSoup(text, 'html.parser')

# <h3 class="midpage">This is a midpage heading.</h3>
midpage = soup.find('h3', {'class': 'midpage'})
print(midpage.text)

# print(soup)

# Expected Output:

# This is a midpage heading.

