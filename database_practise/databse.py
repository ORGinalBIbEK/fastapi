import sqlite3

conn=sqlite3.connect('student.txt')
##conn=sqlite3.connect(':memory:')

c=conn.cursor()
'''
many_student=[(3,'Bibek',11,2322),
              (4,'Sam',22,2011),
              (5,'Shubham',23,2012)]
#create a table

#NUL,INTERGER,REAL(DECIMAL),TEXT,BLOBL(IMAGES,MP3)
#commit our commit
c.executemany("INSERT INTO students VALUES (?,?,?,?)",many_student)
print("command executed succesfully")
'''
c.execute("""CREATE TABLE IF NOT EXISTS students(
    id   INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age  INTEGER NOT NULL,
    year INTEGER NOT NULL
)""")
many_student=[(3,'Bibek',11,2322),
              (4,'Sam',22,2011),
              (5,'Shubham',23,2012)]
c.executemany("INSERT OR IGNORE INTO students VALUES (?,?,?,?)",many_student)
print("command executed succesfully")

conn.commit()
c.execute("SELECT * FROM students")
 # 1. Renamed to 'all_students' so we don't overwrite Python's built-in keywords
all_students = c.fetchall()

print("\n--- Printing whole tuples ---")
for all_students in all_students:   
    print(all_students)

print("\n--- Printing specific columns combined ---")
for all_student in all_students:
   print(f"{all_students[1]} {all_students[2]}")

#close
conn.close()