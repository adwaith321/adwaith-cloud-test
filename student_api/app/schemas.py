from pydantic import BaseModel
from typing import Optional, List
from datetime import date

class StudentCreate(BaseModel):
    first_name: str
    last_name: str
    middle_name: Optional[str]
    age: int
    city: str

class Student(StudentCreate):
    id: int
    class Config:
        orm_mode = True

class ClassCreate(BaseModel):
    class_name: str
    description: str
    start_date: date
    end_date: date
    number_of_hours: int

class Class(ClassCreate):
    id: int
    class Config:
        orm_mode = True
