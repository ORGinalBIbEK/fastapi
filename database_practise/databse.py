import sqlite3

conn=sqlite3.connect('student.txt')
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