from pydantic import BaseModel


class User(BaseModel):
    firstName: str
    email: str
    password: str


class UserPost(BaseModel):
    firstName: str
    email: str
    password: str
    confirmPassword: str