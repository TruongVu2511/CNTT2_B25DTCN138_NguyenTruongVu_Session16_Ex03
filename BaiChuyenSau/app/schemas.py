from pydantic import BaseModel
from datetime import datetime
from typing import List

class CourseBase(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

class StudentBase(BaseModel):
    id: int
    full_name: str
    courses: List[CourseBase] = []

    class Config:
        from_attributes = True

class EnrollmentBase(BaseModel):
    id: int
    student_id: int
    course_id: int
    enrolled_at: datetime

    class Config:
        from_attributes = True
