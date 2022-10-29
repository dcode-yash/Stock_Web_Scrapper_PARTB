import sqlite3

conn = sqlite3.connect('stocksdata_2.db')
c = conn.cursor()
c.execute('''SELECT * FROM data ''')
results = c.fetchall()
print(results)
conn.close()
