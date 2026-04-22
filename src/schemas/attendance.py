from pydantic import BaseModel
from uuid import UUID 
from typing import Optional 
from datetime import datetime 
from enum import Enum 

class AttendanceStatus(str, Enum):
    present = "Present"
    absent = "Absent"
    late = "Late"

class AttendanceBase(BaseModel):
    name: str 
    session_id: UUID 
    student_id: UUID 
    status: AttendanceStatus 
    marked_at: datetime 


class AttendanceCreate(AttendanceBase):
    pass 


class AttendanceRead(AttendanceBase):
    id: UUID 


class AttendanceUpdate(BaseModel):
    status: Optional[AttendanceStatus] = None 