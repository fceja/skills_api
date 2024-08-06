from sqlalchemy import Column, Integer, String

from app.models.base import Base


class Language(Base):
    __tablename__ = "languages"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    def __init__(self, language_data):
        self.name = language_data.name
