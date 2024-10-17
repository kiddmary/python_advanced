import sqlite3
def sql_to_csv(db_filename, table_name, csv_filename):

    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()
    query = 'SELECT * FROM ' + table_name
    cursor.execute(query)
    # conn.commit()
    # desc = c.description
    conn.close()

    return query

db_name = '../session_2.db'
table_name = 'revenue'
csv_filename = 'revenue_from_db.csv'

myresult = sql_to_csv(db_name, table_name, csv_filename)
print(myresult)