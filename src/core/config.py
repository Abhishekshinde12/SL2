from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os 
from functools import lru_cache
load_dotenv()

class Settings(BaseSettings):
    DATABASE_URL: str =  os.getenv('DATABASE_URL')
    ACCESS_TOKEN_EXPIRY_TIME: int = os.getenv('ACCESS_TOKEN_EXPIRY_TIME') 
    ACCESS_TOKEN_SECRET_KEY: str = os.getenv('ACCESS_TOKEN_SECRET_KEY') 
    REFRESH_TOKEN_EXPIRY_TIME: int = os.getenv('REFRESH_TOKEN_EXPIRY_TIME') 
    REFRESH_TOKEN_SECRET_KEY: str = os.getenv('REFRESH_TOKEN_SECRET_KEY') 
    ALGORITHM: str = os.getenv('ALGORITHM') 


@lru_cache
def get_settings() -> Settings:
    return Settings()

settings = get_settings()