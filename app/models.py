from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

class BaseUser(BaseModel):
    id: str

class User(BaseUser):
    name: str
    password: str
