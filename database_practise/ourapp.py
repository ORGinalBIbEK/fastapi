import database3


#adding record to the table
#database3.add_student(9,'Abiskar',19,2023)


#deleting a record from the table
#database3.delete_student('9')
stuff=[
    (10,'Bibek',9,2026),
    (11,'Hari',39,2006),
    (12,'Ram',29,2016)
]
database3.many_student(stuff)
#showing all the records
database3.show_all()

