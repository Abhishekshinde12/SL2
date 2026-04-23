from core.config import settings
from sqlmodel import Session, create_engine

# create engine to actual handle connections
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True
    )

# creating postgres client as depedency here
def get_session():
    with Session(engine) as session:
        yield session