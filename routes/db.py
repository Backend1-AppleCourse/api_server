from fastapi import APIRouter
from utils.db import get_all_students, get_student, create_student, get_all_students_in_class

router = APIRouter()

@router.get("/db/all-students")
async def read_items():
    return await get_all_students()

@router.get("/db/{item_id}")
async def read_item(item_id: int):
    return {"id": item_id, "student": await get_student(item_id)}

@router.post("/db/create-student")
async def create_item(item: dict):
    await create_student(item)
    return {"name": item.get("name"), "id": item.get("description"), "age": item.get("age"), "classes": item.get("classes")}

@router.get("/db/class-students/{class_name}")
async def read_item(class_name: str):
    return {"class_name": class_name, "students": await get_all_students_in_class(class_name)}