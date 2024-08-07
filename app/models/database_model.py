from sqlalchemy import Column, Integer, String

from app.models.base import Base


class Database(Base):
    __tablename__ = "database"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    def __init__(self, database_data):
        self.name = database_data.name
