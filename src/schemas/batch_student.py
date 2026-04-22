from pydantic import BaseModel
from uuid import UUID 

class BatchStudentBase(BaseModel):
    batch_id: UUID 
    student_id: UUID 

class BatchStudentCreate(BatchStudentBase):
    pass

class BatchStudentRead(BatchStudentBase):
    pass