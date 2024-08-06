from sqlalchemy import Column, ForeignKey, Integer

from app.models.base import Base


# associative table
class UserSkill(Base):

    __tablename__ = "user_skills"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    language_id = Column(Integer, ForeignKey("languages.id"))
    frontend_tool_id = Column(Integer, ForeignKey("frontend_tools.id"), nullable=True)

    def __init__(self, user_skills):
        self.user_id = user_skills.user_id
        self.language_id = user_skills.language_id
        self.frontend_tool_id = user_skills.frontend_tool_id
