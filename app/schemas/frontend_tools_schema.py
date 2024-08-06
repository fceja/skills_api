from pydantic import BaseModel


class FrontendToolsBase(BaseModel):
    name: str


class FrontendToolsCreate(FrontendToolsBase):
    pass


class FrontendToolsRead(FrontendToolsBase):
    pass
