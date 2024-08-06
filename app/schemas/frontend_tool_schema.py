from pydantic import BaseModel


class FrontendToolBase(BaseModel):
    name: str


class FrontendToolCreate(FrontendToolBase):
    pass


class FrontendToolRead(FrontendToolBase):
    pass
