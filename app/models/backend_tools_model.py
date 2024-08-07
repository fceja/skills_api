from sqlalchemy import Column, Integer, String

from app.models.base import Base


class BackendTool(Base):
    __tablename__ = "backend_tools"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    def __init__(self, backend_tool_data):
        self.name = backend_tool_data.name
