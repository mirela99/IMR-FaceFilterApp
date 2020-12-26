
import sqlite3 as sl

con = sl.connect('my-test.db')


# sql = 'INSERT INTO USER (id, username, password) values(?, ?, ?)'
# data = [
#     (1, 'Alice', 'asdas'),
#     (2, 'Bob', '22'),
# #     (3, 'Chris', '23')
# # ]
#
# with con:
#     con.executemany(sql, data)
#
