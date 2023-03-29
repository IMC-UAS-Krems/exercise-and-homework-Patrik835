import sqlite3
from session3 import create_db
import pytest

@pytest.fixture
def f_database():
    create_db("session3.db")
    conn = sqlite3.connect("session3.db")
    c= conn.cursor()
    c.execute("INSERT INTO Professor VALUES(123, 'name', 'g101','ss')")
def test_1(f_database):
    conn = sqlite3.connect("session3.db")
    c= conn.cursor()
    c.execute("SELECT * FROM Professor")
    assert c.fetchone() == (123, 'name', 'g101','ss')