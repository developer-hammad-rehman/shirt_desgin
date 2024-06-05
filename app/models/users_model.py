from typing import Optional
from sqlmodel import Field , SQLModel

class Users (SQLModel , table=True):
    id : Optional[int] = Field(default=None , primary_key=True)
    username : str
    password : str