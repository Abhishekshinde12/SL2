from sqlmodel import SQLModel, Field 
from uuid import UUID, uuid4 
from datetime import datetime 

class BatchInvite(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    batch_id: UUID = Field(foreign_key='batch.id')
    token: str 
    created_by: UUID = Field(foreign_key='user.id')
    expires_at: datetime
    used: bool = False