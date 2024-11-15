# 2.29:  Connect to a database and generate a cursor object.

# Remember that from exercise files, any data file will be located in the parent directory.  So the
# correct location for this week's database file is session_2.db.

# Confirm that you have connected to the existing database with this query:

# SELECT name FROM sqlite_master WHERE type= "table"

import runreport
import sqlite3
conn = sqlite3.connect('../session_2.db')

c = conn.cursor()

c.execute('SELECT name FROM sqlite_master WHERE type = "table"')

row = c.fetchall()
print(row)

conn.close()
# Expected Output:

# ('ad_companies',)
# ('ad_buys',)
# ('students',)
# ('revenue',)
# ('student_status',)
# ('user',)
# ('user_classes',)
# ('companyrev',)
# ('planets',)

