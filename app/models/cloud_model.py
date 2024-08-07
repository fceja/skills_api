from sqlalchemy import Column, Integer, String

from app.models.base import Base


class Cloud(Base):
    __tablename__ = "clouds"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    def __init__(self, cloud_data):
        self.name = cloud_data.name
