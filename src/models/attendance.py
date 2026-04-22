from sqlmodel import SQLModel, Field 
from uuid import UUID, uuid4 
from datetime import datetime, timezone 

class Attendance(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str 
    session_id: UUID = Field(foreign_key='session.id')
    student_id: UUID = Field(foreign_key='user.id')
    status: str 
    marked_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))