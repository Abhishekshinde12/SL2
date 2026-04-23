from pydantic import BaseModel 
from uuid import UUID 
from datetime import datetime 
from typing import Optional

class InstitutionBase(BaseModel):
    name: str 
    created_by: UUID 

class InstitutionCreate(InstitutionBase):
    pass 

class InstitutionRead(InstitutionBase):
    id: UUID 
    created_at: datetime 

class InstitutionUpdate(BaseModel):
    name: Optional[str] = None 