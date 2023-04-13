import sqlite3

create_table_person = '''CREATE TABLE IF NOT EXISTS Person(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(50),
        Age INTEGER CHECK (Age > -1),
        gender CHAR CHECK (gender IN ("M","F","0")))'''
create_table_frequents = '''CREATE TABLE IF NOT EXISTS Frequents (
        person_id INTEGER NOT NULL,
        pizzeria VARCHAR(255) NOT NULL,
        PRIMARY KEY (person_id, pizzeria),
        FOREIGN KEY (person_id) REFERENCES Person(id))'''
create_table_eats = '''CREATE TABLE IF NOT EXISTS Eats (
        person_id INTEGER NOT NULL,
        pizza VARCHAR(255) NOT NULL,
        PRIMARY KEY (person_id, pizza),
        FOREIGN KEY (person_id) REFERENCES Person(id))'''
create_table_serves = '''CREATE TABLE IF NOT EXISTS Serves (
        pizzeria VARCHAR(255) NOT NULL,
        pizza VARCHAR(255) NOT NULL,
        price NUMERIC(4,2)
        PRIMARY KEY (pizzeria, pizza))'''

def create_database(file_name):
    conn = sqlite3.connect(file_name)
    try:
        c = conn.cursor()
        c.execute(create_table_person)
        c.execute(create_table_frequents)
        c.execute(create_table_eats)
        c.execute(create_table_serves)
        conn.commit()
    finally:
        conn.close()


create_database('session5.db')