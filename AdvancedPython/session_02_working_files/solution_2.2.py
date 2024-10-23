"""
    solution_2.2.py -- Drop table before creating one
    Author:  Mary Kidd (kiddmary@gmail.com)
    Last Revised:  10/21/2024
"""

import sqlite3

conn = sqlite3.connect('session_2.db')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS weather_newyork')
cursor.execute('CREATE TABLE weather_newyork ( date TEXT, mean_temp INT, precip REAL, events TEXT)')
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")

conn.commit()