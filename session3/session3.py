import sqlite3

def create_db(name):
    conn = sqlite3.connect(name)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS Professor (PersNr Integer PRIMARY KEY , Name TEXT, Room TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS Assistant (PersNr PRIMARY KEY , Name Text , Expertise Text )")
    c.execute("CREATE TABLE IF NOT EXISTS Student (MatNr Integer PRIMARY KEY , Name TEXT, Semester Integer)")
    c.execute("CREATE TABLE IF NOT EXISTS Lecture (LectNr Integer PRIMARY KEY , Title TEXT, ECTS Integer)")
    #,Assist Integer, FOREIGN KEY (Assist) REFERENCES Assistant (PersNr) 
