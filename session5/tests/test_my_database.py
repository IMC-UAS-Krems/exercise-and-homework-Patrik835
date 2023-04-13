import sqlite3


def test_empty_db(empty_db_file):
    conn = sqlite3.connect(empty_db_file)
    c = conn.cursor()
    c.execute("SELECT * FROM sqlite_master WHERE type='table'")
    result = c.fetchall()
    assert len(result) == 4

