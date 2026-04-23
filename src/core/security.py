import jwt 
from jwt.exceptions import InvalidTokenError
from datetime import datetime, timezone, timedelta
from src.core.config import settings 
from typing import Dict, Any
from pwdlib import PasswordHash


'''PASSWORD UTILITY'''
password_hash = PasswordHash.recommended()

def hash_password(password):
    return password_hash.hash(password)
    
def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)


'''JWT CODE'''
# create refresh and access token and decode function
def create_access_token(user_id: str, role: str) -> str:
    payload = {
        "sub": user_id,
        "role": role,
        "type": "access",
        "iat": datetime.now(timezone.utc),
        "exp": datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRY_TIME)
    }
    return jwt.encode(payload, settings.ACCESS_TOKEN_SECRET_KEY, settings.ALGORITHM)


def create_refresh_token(user_id: str, role: str) -> str:
    payload = {
        "sub": user_id,
        "role": role,
        "type": "refresh",
        "iat": datetime.now(timezone.utc),
        "exp": datetime.now(timezone.utc) + timedelta(minutes=settings.REFRESH_TOKEN_EXPIRY_TIME)
    }
    return jwt.encode(payload, settings.REFRESH_TOKEN_SECRET_KEY, settings.ALGORITHM)


def decode_token(token: str, token_type: str = "access") -> Dict[str, Any]:
    try:
        secret = settings.ACCESS_TOKEN_SECRET_KEY if token_type == "access" else settings.REFRESH_TOKEN_SECRET_KEY
        return jwt.decode(token, secret, settings.ALGORITHM)
    except InvalidTokenError as e:
        print(f"Validation failed: {e}")
        raise