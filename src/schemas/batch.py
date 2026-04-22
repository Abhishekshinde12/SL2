from pydantic import BaseModel
from uuid import UUID 
from typing import Optional 
from datetime import datetime 

class BatchBase(BaseModel):
    name: str 
    institution_id: UUID 

class BatchCreate(BatchBase):
    pass 

class BatchRead(BatchBase):
    id: UUID 
    created_at: datetime 

class BatchUpdate(BaseModel):
    name: Optional[str] = None 
    institution_id: Optional[str] = None 