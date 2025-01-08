from pydantic import BaseModel, EmailStr, conint
from typing import Annotated

class UserSchema(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: Annotated[int, conint(ge=0, le=1)]

    class Config:
        from_attributes = True

class UserCreateSchema(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: Annotated[int, conint(ge=1, le=2)] = 2

class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str
