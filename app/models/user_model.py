from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.models.base import Base
from app.models.user_language_model import user_language


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    languages = relationship(
        "Language", secondary=user_language, back_populates="users"
    )
