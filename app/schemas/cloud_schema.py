from pydantic import BaseModel


class CloudBase(BaseModel):
    name: str


class CloudCreate(CloudBase):
    pass


class CloudRead(CloudBase):
    pass
