import sqlite3

def test_s2_1():
    try:
        conn = sqlite3.connect("test-db.db")
        c = conn.cursor()
        c.execute("DROP TABLE IF EXISTS Professor")
        c.execute("CREATE TABLE IF NOT EXISTS Professor (PersNr Integer PRIMARY KEY , FirstName TEXT, LastName TEXT)")
        c.execute("INSERT INTO Professor VALUES(123,'Foo','Bar')")
        c.execute("INSERT INTO Professor VALUES(123,'Foo','Bar')")
    finally:
        conn.commit()
        conn.close()
def test_s2_2():
    conn = sqlite3.connect("test-db.db")
    c = conn.cursor()
    c.execute("INSERT INTO Professor VALUES(234,'Donald','Duck')")
    print(c.execute("SELECT * FROM Professor").fetchall())
    conn.commit()
    conn.close()