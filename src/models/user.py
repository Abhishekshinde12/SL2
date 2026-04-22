from sqlmodel import SQLModel, Field 
from datetime import datetime, timezone
from uuid import UUID, uuid4
from pydantic import EmailStr

class User(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str 
    email: EmailStr = Field(unique=True, index=True)
    hashed_password: str 
    role: str 
    institution_id: UUID = Field(default=None, foreign_key='institution.id')
    created_at: datetime = Field(default_factory= lambda: datetime.now(timezone.utc))