from pydantic import BaseModel, model_validator
from uuid import UUID 
from typing import Optional 
from datetime import datetime 

class SessionBase(BaseModel):
    batch_id: UUID 
    trainer_id: UUID 
    title: str 
    date: datetime 
    start_time: str 
    end_time: str

class SessionCreate(SessionBase):
    # assuring end date comes after start date
    @model_validator(mode='after')
    def end_after_start(self) -> 'SessionCreate':
        if self.end_time <= self.start_time:
            raise ValueError('end_time must be after start_time')
        return self

class SessionRead(SessionBase):
    id: UUID 
    created_at: datetime 

class SessionUpdate(BaseModel):
    title: Optional[str] = None
    date: Optional[datetime] = None
    start_time: Optional[str] = None
    end_time: Optional[str] = None