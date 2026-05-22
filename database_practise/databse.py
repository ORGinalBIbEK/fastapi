import sqlite3

conn=sqlite3.connect('student.db')
##conn=sqlite3.connect(':memory:')

c=conn.cursor()


#create a table
'''c.execute("""CREATE TABLE students(
    id   INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age  INTEGER NOT NULL,
    year INTEGER NOT NULL
)""")'''
#NUL,INTERGER,REAL(DECIMAL),TEXT,BLOBL(IMAGES,MP3)
#commit our commit
c.execute("INSERT INTO students VALUES (01, 'John', 20, 2021)")
conn.commit()

#close
conn.close()