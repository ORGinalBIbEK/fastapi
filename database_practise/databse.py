import sqlite3

conn=sqlite3.connect('student.db')
##conn=sqlite3.connect(':memory:')

c=conn.cursor()

c.execute("SELECT * FROM students")
#c.fetchone()
#c.fetchmany()
#c.fetchall()
print(c.fetchone()[3])

conn.commit()

#close
conn.close()