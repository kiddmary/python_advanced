"""
 homework_5.3.py -- Sort list of dicts by mean temperature

 Author: Mary Kidd (kiddmary@gmail.com)
 Last Revised: 11/12/2024
"""

import json

def by_mean_temp(arg):
    return int(arg['mean_temp'])

fh = open('weny_lod_tiny.json')
lod = json.load(fh)

sorted_dicts = sorted(lod, key=by_mean_temp)

for idict in sorted_dicts:
    print(idict)