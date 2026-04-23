from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4
from datetime import datetime, timezone 


class Institution(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str 
    created_by: UUID #removed FK constraint for cycle removal
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))