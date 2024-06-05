from sqlmodel import Session
from typing import Annotated
from app.db.engine import engine
from fastapi import Depends

def get_session():
    with Session(engine) as session:
        yield session


DBSESSION = Annotated[Session , Depends(get_session)]