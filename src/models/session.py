from sqlmodel import SQLModel, Field 
from uuid import UUID, uuid4 
from datetime import datetime, timezone 

class Session(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    batch_id: UUID = Field(foreign_key='batch.id')
    trainer_id: UUID = Field(foreign_key='trainer.id')
    title: str 
    date: datetime 
    start_time: str
    end_time: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))