"""
 homework_5.4.py -- Sort dict of dicts by mean temperature

 Author: Mary Kidd (kiddmary@gmail.com)
 Last Revised: 11/12/2024
"""

import json

def by_mean_temp(key):
    return int(dod[key]['mean_temp'])

fh = open('weny_dod_tiny.json')
dod = json.load(fh)

keys = sorted(dod, key=by_mean_temp)

for key in keys:
    print(f'{key}:  {dod[key]}')