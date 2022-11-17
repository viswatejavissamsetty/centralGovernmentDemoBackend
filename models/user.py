from pydantic import BaseModel


class User(BaseModel):
    fullName: str
    email: str
    mobileNumber: str
    dob: str
    password: str


class UserPost(BaseModel):
    fullName: str
    email: str
    mobileNumber: str
    dob: str
    password: str
    confirmPassword: str

class UpdateUser(BaseModel):
    fullName: str
    dob: str

class LoginUser(BaseModel):
    email: str
    password: str
