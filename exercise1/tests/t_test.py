import sqlite3
import os

# def test_square():
#     assert True==True
def check_e():
    try:
        with open('exercise.1.db', 'r'):
            pass
    except FileNotFoundError:
        assert False, "Database file not found."
    assert True, "Database exists"

def test_database_file_exists():
    assert os.path.exists('exercise1/exercise1.db')

# def test_list_tables():
#     conn = sqlite3.connect('exercise1.db')
#     cursor = conn.cursor()
#     cursor.execute("CREATE TABLE Test(Id, Desc)")
#     tables = cursor.fetchall()
#     cursor.close()
#     conn.close()
#     assert len(tables) > 0, "No tables found in database."
