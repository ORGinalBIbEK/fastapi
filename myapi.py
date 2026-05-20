
'''
GET - GET AN INFORMATION\
POST- CREATE SOMETHING NEW
PUT- UPDATE
DELETE- DELETE SOMETHING 
'''
from fastapi import FastAPI

app=FastAPI()

student ={
    1:{
        "name":"bibek",
        "age":19,
        "class":"bachelor"
    }

}
@app.get("/")
def index():
    return {"name":"FIRST DATA"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int):
    return student[student_id]