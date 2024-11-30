# app/routes/student.py
from fastapi import APIRouter, HTTPException, Query
from app.models.studentModel import Student
from app.db.connection import students_collection
from typing import Optional
from bson import ObjectId

router = APIRouter()

@router.post("/students", response_model=dict, status_code=201)
async def create_student(student: Student):
    student_data = student.dict()
    try:
        result = students_collection.insert_one(student_data)
        inserted_student_id = str(result.inserted_id)
        return {"id": inserted_student_id}
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error creating student: {str(e)}")

@router.get("/students", response_model=dict, status_code=200)
async def get_students(
    country: Optional[str] = Query(None, description="Filter students by country."),
    age: Optional[int] = Query(None, ge=0, description="Filter students by age, greater than or equal to the provided age.")):
    
    query = {}
    if country:
        query["address.country"] = country
    if age is not None:
        query["age"] = {"$gte": age}
    try:
        students_cursor = students_collection.find(query)
        students_list = []
        for student in students_cursor:
            student_data = {
                "name": student["name"],
                "age": student["age"]
            }
            students_list.append(student_data)
        return {"data": students_list}

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error fetching students: {str(e)}")
    
@router.get("/students/{id}", response_model=Student, status_code=200)
async def get_student_by_id(id: str):
    try:
        if not ObjectId.is_valid(id):
            raise HTTPException(status_code=400, detail="Invalid student ID format")
        
        student = students_collection.find_one({"_id": ObjectId(id)})

        if not student:
            raise HTTPException(status_code=404, detail="Student with {id} not found")

        student['_id'] = str(student['_id'])
        return student
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error fetching student: {str(e)}")
    
@router.patch("/students/{id}", status_code=204)
async def update_student(id: str, student: Student):
    try:
        if not ObjectId.is_valid(id):
            raise HTTPException(status_code=400, detail="Invalid student ID format")
        
        update_data = student.dict(exclude_unset=True)
        
        if not update_data:
            return {}
        
        result = students_collection.update_one({"_id": ObjectId(id)}, {"$set": update_data})
        
        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="Student with {id} not found")
        
        return {}
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error updating student: {str(e)}")
    
@router.delete("/students/{id}", status_code=200)
async def delete_student(id: str):
    try:
        if not ObjectId.is_valid(id):
            raise HTTPException(status_code=400, detail="Invalid student ID format")
        
        student = students_collection.find_one({"_id": ObjectId(id)})

        if not student:
            raise HTTPException(status_code=404, detail="Student with {id} not found")

        students_collection.delete_one({"_id": ObjectId(id)})

        return {}
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error deleting student: {str(e)}")