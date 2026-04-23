from src.db.postgres_db import get_session
from sqlmodel import Session 
from typing import Annotated
from fastapi import Depends

# Session Dependency here
SessionDep = Annotated[Session, Depends(get_session)]