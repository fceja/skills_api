from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.models.base import Base


# associative table
class UserSkill(Base):

    __tablename__ = "user_skills"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    cloud_id = Column(Integer, ForeignKey("clouds.id"))
    language_id = Column(Integer, ForeignKey("languages.id"))
    database_id = Column(Integer, ForeignKey("database.id"), nullable=True)
    frontend_tool_id = Column(Integer, ForeignKey("frontend_tools.id"), nullable=True)
    backend_tool_id = Column(Integer, ForeignKey("backend_tools.id"), nullable=True)

    user = relationship("User", back_populates="skills")
    language = relationship("Language")
    cloud = relationship("Cloud")
    database = relationship("Database")
    frontend_tool = relationship("FrontendTool")
    backend_tool = relationship("BackendTool")

    def __init__(self, user_skills):
        self.user_id = user_skills.user_id
        self.cloud_id = user_skills.cloud_id
        self.database_id = user_skills.database_id
        self.language_id = user_skills.language_id
        self.frontend_tool_id = user_skills.frontend_tool_id
        self.backend_tool_id = user_skills.backend_tool_id
