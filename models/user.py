from pydantic import BaseModel


class User(BaseModel):
    firstName: str
    email: str
    password: str
