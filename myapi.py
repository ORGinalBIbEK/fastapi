
'''
GET - GET AN INFORMATION\
POST- CREATE SOMETHING NEW
PUT- UPDATE
DELETE- DELETE SOMETHING 
'''
from fastapi import FastAPI, Path
from typing import Optional
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

def get_student(student_id: int=Path(...,description="The Id of the student you wanna view"),gt=0,lt=3):
    return student[student_id]

@app.get("/get-by-name")
def get_student(*, name: Optional[str]=None,test : int):
    for student_id in student:
        if student[student_id]["name"]==name:
            return student[student_id]
    return {"data":"Not Found"}