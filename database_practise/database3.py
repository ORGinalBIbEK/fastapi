import sqlite3

conn=sqlite3.connect('student.txt')
##conn=sqlite3.connect(':memory:')

c=conn.cursor()

def show_all():
    #query the database
    c.execute("SELECT * FROM students")
    db_students = c.fetchall()

    for db_students in db_students:   
        print(db_students)
        
    conn.commit()

    conn.close()


#add a new record to the table
def add_student(id,name,age,year):
    conn=sqlite3.connect('student.txt')
    c=conn.cursor()
    c.execute("INSERT OR IGNORE INTO students VALUES (?,?,?,?)",(id,name,age,year))
    conn.commit()
    conn.close()

#add a many record to the table
def many_student(list):
    conn=sqlite3.connect('student.txt')
    c=conn.cursor()
    c.executemany("INSERT OR IGNORE INTO students VALUES (?,?,?,?)",(list))
    conn.commit()
    conn.close()

def delete_student(id):
    conn=sqlite3.connect('student.txt')
    c=conn.cursor()
    c.execute(" DELETE from students WHERE id =(?)",id)
    conn.commit()
    conn.close()
