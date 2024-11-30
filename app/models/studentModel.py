from pydantic import BaseModel, Field
from typing import Dict

class Student(BaseModel):
    name: str = Field(..., description="The full name of the student (max 100 characters).")
    age: int = Field(..., ge=0, description="The age of the student. Must be between 0 and 120 years.")
    address: Dict[str, str] = Field(..., description="The student's address, which must include 'city' and 'country' as keys. Both values must be strings with a maximum length of 100 characters.")
