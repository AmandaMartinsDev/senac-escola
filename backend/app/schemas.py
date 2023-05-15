from typing import Optional

from pydantic import BaseModel


class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str
    
    
class TokenPayload(BaseModel):
    sub: str = None
    exp: int = None


class UserBase(BaseModel):
    user_name: str
    user_type: str
    document_id: str
    user_address: str
    user_phone: int


class UserCreate(UserBase):
    user_email: str
    user_password: str


class UserUpdate(UserBase):
    user_email: Optional[str] = None
    user_password: Optional[str] = None
    user_name: Optional[str] = None
    user_type: Optional[str] = None
    document_id: Optional[str] = None
    user_address: Optional[str] = None
    user_phone: Optional[int] = None


class UserRead(UserBase):
    user_email: str

    class Config:
        orm_mode = True
