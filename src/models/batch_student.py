from sqlmodel import SQLModel, Field 
from uuid import UUID

# junction table, (batch + student) => unique record
class BatchStudent(SQLModel, table=True):
    batch_id: UUID = Field(foreign_key='batch.id', primary_key=True)
    student_id: UUID = Field(foreign_key='user.id', primary_key=True)