from typing import Optional

from fastapi import FastAPI, Path

from py_models import Student, UpdateStudent

app = FastAPI()

students = {
    1: {
        "name": "john",
        "age": 17,
        "class": "year 12"
    },
    2: {
        "name": "marty",
        "age": 16,
        "class": "year 12"
    },
    3: {
        "name": "mary",
        "age": 16,
        "class": "year 11"
    },
}


@app.get("/")
def index():
    return {"name": "First Data"}


@app.get("/student/{student_id}")
def get_student(student_id: int = Path(description="The ID of the student you want to view",
                                       gt=0, le=50)):
    return students[student_id]


@app.get("/get-by-name")
def get_student_by_name(name: Optional[str] = ''):
    for student in students:
        if students[student]['name'] == name:
            return students[student]

    return {"Error": f'{name} not found'}


@app.put("/create-student/{student_id}")
def update_student(student_id: int, student_info: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student not found"}

    for info in student_info:
        if info[1]:
            students[student_id][info[0]] = info[1]

    return students[student_id]


@app.post("/create-student/{student_id}")
def create_student(student_id: int, student_info: Student):
    if student_id in students:
        return {"Error": "Student already exists"}

    students[student_id] = student_info
    return students[student_id]


@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student does not exists"}

    del students[student_id]
    return students
