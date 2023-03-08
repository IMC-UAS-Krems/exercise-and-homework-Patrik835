import sqlite3
import os



def square(f):
    return f*f
def test_square():
    assert square(5) == 24

def pass_():
    return True
def test_pass():
    assert pass_()
def check_e():
    try:
        with open('exercise1/exercise1.db'):
            pass
    except FileNotFoundError:
        "No file"
    return "File exists"
def test_check():
    if "No file" in check_e():
        assert False
    else:
        assert True

# def test_database_file_exists():
#     assert os.path.exists('exercise1/exercise1.db')

# def test_list_tables():
#     conn = sqlite3.connect('exercise1.db')
#     cursor = conn.cursor()
#     cursor.execute("CREATE TABLE Test(Id, Desc)")
#     tables = cursor.fetchall()
#     cursor.close()
#     conn.close()
#     assert len(tables) > 0, "No tables found in database."
