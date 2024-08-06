from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.models.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    skills = relationship("UserSkill", back_populates="user")

    def __init__(self, user_data):
        self.name = user_data.name
        self.email = user_data.email
