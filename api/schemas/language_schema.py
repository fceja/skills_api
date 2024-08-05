from pydantic import BaseModel


class LanguageBase(BaseModel):
    name: str


class LanguageCreate(LanguageBase):
    pass


class LanguageRead(LanguageBase):
    pass
