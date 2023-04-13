import sqlite3
import pytest
from setup_database import create_database


@pytest.fixture
def empty_db(temp_path):
    file_name = temp_path / 'session5.db'
    create_database(file_name)
    return file_name

@pytest.fixture
def test_db_input(empty_db,random_pesrons):
    conn = sqlite3.connect(empty_db)
    c = conn.cursor()
    c.executemany('''INSERT INTO Person(name,age,gender) VALUES ('Bob', 22, 'M')''', random_pesrons) 
    c.execute('''INSERT INTO Frequents VALUES ('John', 'Pizza Hut')''')
    c.execute('''INSERT INTO Eats VALUES ('John', 'Cheese Pizza')''')
    c.execute('''INSERT INTO Serves VALUES ('Pizza Hut', 'Cheese Pizza', 100)''')
    conn.commit()
    conn.close()

