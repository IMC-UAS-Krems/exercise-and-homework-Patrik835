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

def test_file_exist_no_lib():
    try:
        with open("../exercise1.db") as f:
            assert True
    except FileNotFoundError:
        assert False

def test_file_exists():                            #alternative using os lib
    path = "../exercise1.db"
    assert os.path.exists(path)

# def test_list_tables():
#     conn = sqlite3.connect('exercise1.db')
#     cursor = conn.cursor()
#     cursor.execute("CREATE TABLE Test(Id, Desc)")
#     tables = cursor.fetchall()
#     cursor.close()
#     conn.close()
#     assert len(tables) > 0, "No tables found in database."
