from tinydb import TinyDB, Query
from src.logging_db_calls import log_function_data

# This will create a file named db.json in the current directory
db = TinyDB('db/db.json')

@log_function_data
async def get_all_students ():
    return db.all()

@log_function_data
async def get_student(student_id):
    Student = Query()
    return db.search(Student.id == student_id)

@log_function_data
async def create_student(student):
    return db.insert({"name": student.get("name"), "id": student.get("id"), "age": student.get("age"), "classes": student.get("classes")})

@log_function_data
async def get_all_students_in_class(class_name):
    Student = Query()
    return db.search(Student.classes.any(class_name))