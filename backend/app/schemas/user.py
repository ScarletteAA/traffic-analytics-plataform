from pydantic import BaseModel, EmailStr
from uuid import UUID  
from datetime import datetime



class UserCreate(BaseModel):
   name: str
   email: EmailStr
   password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: UUID
    name: str
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True
