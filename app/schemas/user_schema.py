from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    email: str
    language_ids: list[int]


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    id: int

    class Config:
        orm_mode: True
