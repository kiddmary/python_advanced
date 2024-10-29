import requests
from bs4 import BeautifulSoup

url = 'https://davidbpython.com/classfiles/elk.html'

response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

title_tag = soup.find('meta', attrs={'property': 'og:title'})
title_tag_content = title_tag.get('content')

byline_tag = soup.find('meta', attrs={'name': 'byl'})
byline_tag_content = byline_tag.get('content')

date_tag = soup.find('meta', attrs={'property': 'article:modified'})
date_tag_content = date_tag.get('content')[0:10]

paragraph = soup.find_all('p', attrs={'class': 'css-158dogj evys1bk0'})

print()
print(f'Title: {title_tag_content}')
print()
print(f'Byline: {byline_tag_content}')
print()
print(f'Date: {date_tag_content}')
print()

count = 0
for tag in paragraph:
    print(tag.text)
    count += 1

print()
print(f'{count} text paragraphs total')