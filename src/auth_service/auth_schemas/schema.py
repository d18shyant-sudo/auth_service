from pydantic import BaseModel,EmailStr
class SignUp(BaseModel):
    username: str
    emailid: EmailStr
    password: str
class Login(BaseModel):
    emailid: EmailStr
    password: str