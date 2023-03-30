import sqlite3

conn=sqlite3.connect("pizzeria.db")
c=conn.cursor()
# conn.execute('CREATE TABLE IF NOT EXISTS Person (name TEXT PRIMARY KEY, age INT, gender  TEXT CHECK(gender IN ('male', 'female', 'other')')
