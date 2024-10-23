"""
    solution_2.3.py -- Read from CSV, write to SQL
    Author:  Mary Kidd (kiddmary@gmail.com)
    Last Revised:  10/21/2024
"""

import sqlite3
import csv

filename = 'weather_newyork.csv'

fh = open(filename)
reader = csv.reader(fh)
header = next(reader)

conn = sqlite3.connect('session_2.db')
cursor = conn.cursor()
cursor.execute('DROP TABLE IF EXISTS weather_newyork')
cursor.execute('CREATE TABLE weather_newyork ( date TEXT, mean_temp INT, precip REAL, events TEXT)')

query = 'INSERT INTO weather_newyork (date, mean_temp, precip, events) VALUES (?, ?, ?, ?)'

for row in reader:
    if row[17] == 'T':
        row[17] = None
    cursor.execute(query, (row[0], row[1], row[17], row[19]))

conn.commit()
conn.close()