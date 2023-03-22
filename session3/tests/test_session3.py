import sqlite3
from session3 import create_db
import pytest

@pytest.fixture
def test_database():
    create_db("session3.db")
    conn = sqlite3.connect("session3.db")
    c= conn.cursor()
    c.execute("INSERT INTO Professor VALUES(123, 'name', 'g101','ss')")
    