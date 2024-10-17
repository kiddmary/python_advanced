import sqlite3
import csv
def sql_to_csv(db_filename, table_name, csv_filename):

    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()
    query = 'SELECT * FROM ' + table_name
    cursor.execute(query)

    conn.commit()

    desc = cursor.description

    header = []

    for col in desc:
        mycol = col[0]
        header.append(mycol)

    wfh = open(csv_filename, 'w')
    writer = csv.writer(wfh)
    writer.writerow(header)

    for row in cursor:
        writer.writerow(row)

    conn.close()
    wfh.close()

    return header

db_name = 'session_2.db'
table_name = 'revenue'
csv_filename = 'revenue_from_db.csv'

myresult = sql_to_csv(db_name, table_name, csv_filename)
print(myresult)