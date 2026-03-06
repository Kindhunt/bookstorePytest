from pydantic import BaseModel
from typing import List

from backend.models.Book import Book


class User(BaseModel):
    username: str
    password: str
    books: List[Book]