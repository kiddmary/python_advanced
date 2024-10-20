import sqlite3
import json

conn = sqlite3.connect('session_2.db')
cursor = conn.cursor()
cursor.execute('DROP TABLE IF EXISTS weather_newyork')
cursor.execute('CREATE TABLE weather_newyork ( date TEXT, mean_temp INT, precip REAL, events TEXT)')

query = 'INSERT INTO weather_newyork (date, mean_temp, precip, events) VALUES (?, ?, ?, ?)'

fh = open('weather_newyork_dod.json')
dod = json.load(fh)

for ikey in dod:
    date = ikey
    mean_temp = dod[ikey]['mean_temp']
    precip = dod[ikey]['precip']
    if precip == 'T':
        precip == None
    events = dod[ikey]['events']

    cursor.execute(query, (date, mean_temp, precip, events))

query = 'SELECT * FROM weather_newyork LIMIT 10'
cursor.execute(query)

for row in cursor:
    print(row)

conn.close()