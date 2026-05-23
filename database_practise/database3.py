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
