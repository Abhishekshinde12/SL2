from pydantic import BaseModel
from typing import Optional
from datetime import datetime 
from uuid import UUID 

class BatchInviteBase(BaseModel):
    batch_id: UUID 
    token: str 
    created_by: UUID 
    expires_at: datetime 
    used: bool

class BatchInviteCreate(BatchInviteBase):
    pass 

class BatchInviteRead(BatchInviteBase):
    id: UUID 

# as invite can be already sent (maybe not), hence can't allow to update expires_at
class BatchInviteUpdate(BaseModel):
    used: Optional[bool] = None 