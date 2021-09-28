import sqlite3

conn = sqlite3.connect('data-dev.sqlite')
c = conn.cursor()
c.execute("SELECT * FROM users")
print(c.fetchall())
c.close()