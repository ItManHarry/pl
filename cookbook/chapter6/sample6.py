'''
Interacting with a Relational Database
Problem
    You need to select, insert, or delete rows in a relational database.
Solution
    A standard way to represent rows of data in Python is as a sequence of tuples
'''
import os

stocks = [
    ('GOOG', 100, 490.1),
    ('AAPL', 50, 545.75),
    ('FB', 150, 7.45),
    ('HPQ', 75, 33.2),
]
import sqlite3
c_p = os.getcwd()
print(c_p)
p_p = os.path.dirname(c_p)
print(p_p)
db_path = os.path.join(os.path.abspath(os.path.join(p_p, 'data\data.db')))
print(db_path)
db = sqlite3.connect(db_path)
c = db.cursor()
c.execute('create table if not exists portfolio(symbol text, shares integer, price real)')
db.commit()
c.executemany('insert into portfolio values(?, ?, ?)', stocks)
db.commit()
for row in c.execute('select * from portfolio'):
    print(row)