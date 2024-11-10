"""
 homework_4.3.py -- Extract stock symbols and percent change

 Author: Mary Kidd (kiddmary@gmail.com)
 Last Revised: 11/9/2024
"""

import re

with open('market_discussion.txt') as fh:
    text = fh.read()

matchobj = re.findall(r'([A-Z]+),\s([+-]\d+\.\d{2})%', text)

sorted = sorted(matchobj)

for stock_symbol, pct in sorted:
    print(f'{stock_symbol}, {pct}')