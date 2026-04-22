from sqlmodel import SQLModel, Field 
from uuid import UUID, uuid4 
from datetime import datetime, timezone 

class Batch(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str 
    institution_id: UUID = Field(foreign_key='institution.id')
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))