import sqlite3

conn=sqlite3.connect('student.db')
##conn=sqlite3.connect(':memory:')

c=conn.cursor()
'''
many_student=[(3,'Bibek',11,2322),
              (4,'Sam',22,2011),
              (5,'Shubham',23,2012)]
#create a table
c.execute("""CREATE TABLE students(
    id   INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age  INTEGER NOT NULL,
    year INTEGER NOT NULL
)""")
#NUL,INTERGER,REAL(DECIMAL),TEXT,BLOBL(IMAGES,MP3)
#commit our commit
c.executemany("INSERT INTO students VALUES (?,?,?,?)",many_student)
print("command executed succesfully")
'''
many_student=[(3,'Bibek',11,2322),
              (4,'Sam',22,2011),
              (5,'Shubham',23,2012)]
c.executemany("INSERT OR IGNORE INTO students VALUES (?,?,?,?)",many_student)
print("command executed succesfully")

conn.commit()

c.execute("SELECT * FROM students")
print(c.fetchall())


#close
conn.close()