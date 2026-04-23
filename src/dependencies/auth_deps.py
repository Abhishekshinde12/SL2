from sqlmodel import Session
from src.db.postgres_db import get_session
from fastapi import Depends, Request, HTTPException
from src.core.security import decode_token
from src.models.user import User 
from typing import Annotated

def get_current_user(
    request: Request,
    session: Session = Depends(get_session)
) -> User:
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    try:
        payload = decode_token(token, "access")
        if payload.get("type") != "access":
            raise ValueError("Access Token not found")
        user = session.get(User, payload["sub"])
        if not user:
            raise ValueError("No such user present")
        return user 
    except ValueError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")

AuthDep = Annotated[User, Depends(get_current_user)]