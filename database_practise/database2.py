import sqlite3

conn=sqlite3.connect('student2.txt')
##conn=sqlite3.connect(':memory:')

c=conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS students(
    id   INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age  INTEGER NOT NULL,
    year INTEGER NOT NULL
)""")
many_student=[(3,'Bibek',11,2322),
              (4,'Sam',22,2011),
              (5,'Shubham',23,2012),
              (6,'Sarthak',20,2011)]
c.executemany("INSERT OR IGNORE INTO students VALUES (?,?,?,?)",many_student)
print("command executed succesfully")

conn.commit()

# First query
c.execute("SELECT * FROM students WHERE age > 18")

adult_students = c.fetchall()

print("\nStudents age > 18:")
for student in adult_students:
    print(student)

# Second query
c.execute("SELECT * FROM students WHERE name LIKE '%am' ")

name_age = c.fetchall()

print("\nName and Age:")
for student in name_age:
    print(student)


#close
conn.close()