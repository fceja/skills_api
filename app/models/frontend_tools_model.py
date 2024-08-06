from sqlalchemy import Column, Integer, String

from app.models.base import Base


class FrontendTool(Base):
    __tablename__ = "frontend_tools"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    def __init__(self, frontend_tool_data):
        self.name = frontend_tool_data.name
