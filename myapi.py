
'''
GET - GET AN INFORMATION\
POST- CREATE SOMETHING NEW
PUT- UPDATE
DELETE- DELETE SOMETHING 
'''
from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel
app=FastAPI()

student_db={
    1:{
        "name":"bibek",
        "age":19,
        "year":2018
    }

}

class Student(BaseModel):
    name:str
    age:int
    year: int

class UpdateStudent(BaseModel):
    name:Optional[str]=None
    age:Optional[int]=None
    year:Optional[int]=None

@app.get("/")
def index():
    return {"name":"FIRST DATA"}

@app.get("/get-student/{student_id}")
def get_student(
    student_id: int=Path(...,description="The Id of the student you wanna view"),gt=0,lt=3):
    return student_db[student_id]

@app.get("/get-by-name")
def get_student(*,student_id: int, name: Optional[str]=None,test : int):
    for student_id in student_db:
        if student_db[student_id]["name"]==name:
            return student_db[student_id]
    return {"data":"Not Found"}

@app.post("/create-student/{student_id}")
def create_student(student_id: int, student_data: Student): # Renamed parameter
    if student_id in student_db:
        return {"Error": "Student exists"}
    
    # .model_dump() converts the Pydantic object back into a standard Python dict
    student_db[student_id] = student_data.model_dump()
    return student_db[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student_data: UpdateStudent):
    # 1. Check the actual global database
    if student_id not in student_db:
        return {"Error": "Student does not exist"}

    if student_data.name is not None:
        student_db[student_id]["name"] = student_data.name

    if student_data.age is not None:
        student_db[student_id]["age"] = student_data.age

    if student_data.year is not None:
        student_db[student_id]["year"] = student_data.year
        
    return student_db[student_id]