import sqlite3

conn = sqlite3.connect('data-dev.sqlite')
c = conn.cursor()

# c.execute("DROP TABLE IF EXISTS roles;")
# c.execute("DROP TABLE IF EXISTS users;")
# c.execute("""
#     CREATE TABLE roles(
#     id INTEGER PRIMARY KEY ,
#     name TEXT NOT NULL
#     );

#     CREATE TABLE users(
#     id INTEGER PRIMARY KEY,
#     email TEXT NOT NULL,
#     username TEXT NOT NULL,
#     role_id INTEGER,
#     password_hash TEXT NOT NULL,
#     FOREIGN KEY (role_id) REFERENCES roles (id));
#     """)
# c.execute("""
#     CREATE TABLE users(
#     id INTEGER PRIMARY KEY,
#     email TEXT NOT NULL,
#     role_id INTEGER NULL,
#     username TEXT NOT NULL,
#     password_hash TEXT NOT NULL
#     )""")
# get tables name

# conn.commit()

# check tables
# c.execute("SELECT name FROM sqlite_master WHERE type='table';")

# check data on table
# c.execute("SELECT * FROM users;")
# c.execute("SELECT * FROM roles;")

# check columns
# c.execute("PRAGMA table_info(users);")
c.execute("PRAGMA table_info(roles);")

print(c.fetchall())


conn.close()