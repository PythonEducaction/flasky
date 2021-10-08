import sqlite3

class Db:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        # conn = sqlite3.connect('data-dev - Copy.sqlite')
        self.c = self.conn.cursor()

    def drop_table(self):
        self.c.execute("DROP TABLE IF EXISTS roles;")
        # c.execute("DROP TABLE IF EXISTS users;")

    def create_multiple_table(self):
        self.c.executescript("""
            CREATE TABLE roles(
            id INTEGER PRIMARY KEY ,
            name TEXT NOT NULL
            );

            CREATE TABLE users(
            id INTEGER PRIMARY KEY,
            email TEXT NOT NULL,
            username TEXT NOT NULL,
            role_id INTEGER,
            password_hash TEXT NOT NULL,
            FOREIGN KEY (role_id) REFERENCES roles (id));
            """)

    def create_single_table(self):
        # c.execute("""
        #     CREATE TABLE users(
        #     id INTEGER PRIMARY KEY,
        #     email TEXT NOT NULL,
        #     role_id INTEGER NULL,
        #     username TEXT NOT NULL,
        #     password_hash TEXT NOT NULL
        #     )""")

        self.c.execute("""
            CREATE TABLE roles(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            "default" BOOLEAN DEFAULT False NOT NULL,
            permissions INTEGER NULL
            );""")

    def add_column(self, table_name):
        self.c.executescript("""
            ALTER TABLE {}
            ADD COLUMN avatar_hash;
            """.format(table_name))

    def add_column_boolean(self, table_name):
        self.c.executescript("""
            ALTER TABLE {}
            ADD COLUMN "default" BOOLEAN
            """.format(table_name))



    def get_tables_name(self):
        self.c.execute("SELECT name FROM sqlite_master WHERE type='table';")

    def get_data_on_table(self, table_name):
        self.c.execute(f"SELECT * FROM {table_name};")
        # c.execute("SELECT * FROM roles;")

    def get_columns_name_on_table(self, table_name):
        self.c.execute(f"PRAGMA table_info({table_name});")

    def update_value(self, table_name, column):
        self.c.execute(
            """
            UPDATE employees
            SET lastname = 'Smith'
            WHERE employeeid = 3;""")

    def commit(self):
        self.conn.commit()


    def all_result(self):
        print(self.c.fetchall())

    def close_connection(self):
        self.conn.close()



db_name = 'data-dev.sqlite'
table_list = ('users', 'roles', 'posts')
table_name = table_list[0]
my_db = Db(db_name)

# my_db.drop_table()
# get_data_on_table()

# my_db.create_multiple_table()

my_db.get_tables_name()
my_db.all_result()

# my_db.add_column()

# my_db.add_column_boolean(table_name)

# my_db.create_single_table()
# # my_db.commit()

my_db.get_data_on_table(table_name)
my_db.all_result()

my_db.get_columns_name_on_table(table_name)
my_db.all_result()

my_db.close_connection()