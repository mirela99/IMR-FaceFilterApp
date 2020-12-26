
import sqlite3 as sl

con = sl.connect('my-test.db')

with con:
    con.execute("""
        CREATE TABLE USER (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT
        );
    """)

sql = 'INSERT INTO USER (id, username, password) values(?, ?, ?)'
data = [
    (1, 'Alice', 'asdas'),
    (2, 'Bob', '22'),
    (3, 'Chris', '23')
]

with con:
    con.executemany(sql, data)

