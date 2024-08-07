from pydantic import BaseModel


class DatabaseBase(BaseModel):
    name: str


class DatabaseCreate(DatabaseBase):
    pass


class DatabaseRead(DatabaseBase):
    pass
