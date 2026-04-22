from pydantic import BaseModel
from pydantic import EmailStr
from enum import Enum 
from uuid import UUID 
from typing import Optional 
from datetime import datetime 

class UserRole(str, Enum):
    student = 'Student'
    trainer = 'Trainer'
    institution = 'Institution'
    programme_manager = 'Programme_manager'
    monitoring_officer = 'Monitoring_officer'

class UserBase(BaseModel):
    name: str 
    email: EmailStr 
    role: str 
    institution_id: Optional[UUID] = None 

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: UUID 
    created_at: datetime 

class UserUpdate(BaseModel):
    name: Optional[str] = None 
    email: Optional[EmailStr] = None 
    institution_id: Optional[UUID] = None 