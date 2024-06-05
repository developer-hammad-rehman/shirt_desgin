from typing import Optional
from sqlmodel import SQLModel, Field


class Orders(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    item: str
    price: str
    user_id: Optional[int] = Field(default=None, foreign_key="users.id")
