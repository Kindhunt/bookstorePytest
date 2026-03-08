from typing import Optional

from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class User(BaseModel):
    id: Optional[int] = None
    username: str
    email: str
    password: str

class UserId(BaseModel):
    id: int