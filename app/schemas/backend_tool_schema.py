from pydantic import BaseModel


class BackendToolBase(BaseModel):
    name: str


class BackendToolCreate(BackendToolBase):
    pass


class BackendToolRead(BackendToolBase):
    pass
