from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.models.base import Base
from app.models.user_language_model import user_language


class Language(Base):
    __tablename__ = "languages"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    users = relationship("User", secondary=user_language, back_populates="languages")
