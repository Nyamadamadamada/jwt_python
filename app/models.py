from enum import Enum
from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

class BaseUser(BaseModel):
    id: str

class User(BaseUser):
    name: str
    password: str
    role: str

class Payload(BaseModel):
    user_id: str
    role: str
    exp: int
