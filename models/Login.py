from pydantic import BaseModel


class Login(BaseModel):
    username: str
    password: str

class JWTAuth(BaseModel):
    token: str