from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel

app = FastAPI()

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["school"]
teachers_collection = db["teachers"]
students_collection = db["students"]



@app.get("/")
async def hello_world():
    return {"message": "Hello World"}


# Teachers APIs
@app.get("/teachers")
async def get_teachers():
    teachers = teachers_collection.find()
    return [teacher for teacher in teachers]
    


class teachers(BaseModel):
    name: str
    teacher_id: int

@app.post("/teachers")
async def create_teacher(teacher: teachers):
    teachers_collection.insert_one(teacher)
    teachers_collection.append(teacher.dict())
    return {"message": "Teacher created successfully"}


@app.get("/teachers/{teacher_id}")
async def get_teacher(teacher_id: int):
    teacher = teachers_collection.find_one({"teacher_id": teacher_id})
    if teacher:
        return teacher
    else:
        return {"message": "Teacher not found"}



@app.put("/teachers/{teacher_id}")
async def update_teacher(teacher_id: str, name: str):
    teacher = teachers_collection.find_one({"teacher_id": teacher_id})
    if teacher:
        teachers_collection.update_one({"_id": teacher_id}, {"$set": {"name": name}})
        return {"message": "Teacher updated successfully"}
    else:
        return {"message": "Teacher not found"}


@app.delete("/teachers/{teacher_id}")
async def delete_teacher(teacher_id: str):
    teacher = teachers_collection.find_one({"_id": teacher_id})
    if teacher:
        teachers_collection.delete_one({"_id": teacher_id})
        return {"message": "Teacher deleted successfully"}
    else:
        return {"message": "Teacher not found"}


# Students APIs
@app.get("/students")
async def get_students():
    students = students_collection.find()
    return [student for student in students]


class students(BaseModel):
    name: str
    student_id : int
    teacher_id: int

@app.post("/students")
async def create_student(student: students):
    students_collection.insert_one(student)
    return {"message": "Student created successfully"}


@app.get("/students/{student_id}")
async def get_student(student_id: str):
    student = students_collection.find_one({"_id": student_id})
    if student:
        return student
    else:
        return {"message": "Student not found"}


@app.put("/students/{student_id}")
async def update_student(student_id: str, name: str):
    student = students_collection.find_one({"_id": student_id})
    if student:
        students_collection.update_one({"_id": student_id}, {"$set": {"name": name}})
        return {"message": "Student updated successfully"}
    else:
        return {"message": "Student not found"}


@app.delete("/students/{student_id}")
async def delete_student(student_id: str):
    student = students_collection.find_one({"_id": student_id})
    if student:
        students_collection.delete_one({"_id": student_id})
        return {"message": "Student deleted successfully"}
    else:
        return {"message": "Student not found"}


@app.post("/teachers/{teacher_id}/assign")
async def assign_students(teacher_id: str, student_ids: list):
    teacher = teachers_collection.find_one({"_id": teacher_id})
    if teacher:
        students_collection.update_many({"_id": {"$in": student_ids}}, {"$set": {"teacher_id": teacher_id}})
        return {"message": "Students assigned to teacher successfully"}
    else:
        return {"message": "Teacher not found"}


