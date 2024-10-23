"""
    solution_2.3.py -- Read from SQL, write to JSON dictionary
    Author:  Mary Kidd (kiddmary@gmail.com)
    Last Revised:  10/21/2024
"""

import json
import sqlite3

conn = sqlite3.connect('session_2.db')
cursor = conn.cursor()
query = cursor.execute('SELECT * FROM revenue')

for row in cursor:
    name = row[0]
    state = row[1]
    cost = row[2]
    print(name, state, cost)


outer_dict = {}
print(outer_dict)

conn.commit()
conn.close()