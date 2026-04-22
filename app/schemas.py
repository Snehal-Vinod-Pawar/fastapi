from datetime import datetime
from typing import Optional
from pydantic import EmailStr
from pydantic.types import conint
from pydantic import BaseModel

# class Post(BaseModel):
#     title: str
#     content: str
#     published: bool = True
#     rating: Optional[int] = None 

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None 

class PostCreate(PostBase):
    pass

class PostUpdate(PostBase):
    pass

class Post(PostBase):
    id: int
    owner_id: int
    created_at: datetime
    owner: "UserOut"
    class Config:
        from_attributes = True

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)

class PostOut(BaseModel):
    Post: Post
    votes: int
    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None