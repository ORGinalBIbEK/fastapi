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
c.execute("SELECT * FROM students")
 # 1. Renamed to 'all_students' so we don't overwrite Python's built-in keywords
all_students = c.fetchall()

print("\n--- Printing whole tuples ---")
for all_students in all_students:   
    print(all_students)

print("\n--- Printing specific columns combined ---")
for all_student in all_students:
   print(f"{all_students[1]} {all_students[2]}")


#quert the database- order by
c.execute("SELECT * FROM students ORDER BY age")
ordered_students=c.fetchall()
print("\n--Ordered by age--")
for ordered_students in ordered_students:
    print(ordered_students)

#query the database -disascending order
c.execute("SELECT * FROM students ORDER BY age DESC")
disordered_students=c.fetchall()
print("\n--Ordered by age in descending order--")
for disordered_students in disordered_students:
    print(disordered_students)

#query the database -and/or
c.execute("SELECT * FROM students WHERE age>18 AND year<2020")
conditional_student=c.fetchall()
print("\n--by condition--")
for conditional_student in conditional_student:
    print(conditional_student)

#limiting the result:
c.execute("SELECT age, * FROM students ORDER BY age LIMIT 2")
limited_students=c.fetchall()
print("\n--by condition--")
for limited_students in limited_students:
    print(limited_students)
c.execute("SELECT age,*FROM students ORDER BY age DESC LIMIT 4")
limited_students=c.fetchall()
print("\n--by condition--")
for limited_students in limited_students:
    print(limited_students)
conn.close()