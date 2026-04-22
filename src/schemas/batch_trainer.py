from pydantic import BaseModel
from uuid import UUID 

class BatchTrainerBase(BaseModel):
    batch_id: UUID 
    trainer_id: UUID 

class BatchTrainerCreate(BatchTrainerBase):
    pass

class BatchTrainerRead(BatchTrainerBase):
    pass