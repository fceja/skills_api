from pydantic import BaseModel
from typing import Optional


class UserSkillBase(BaseModel):
    user_id: int
    language_id: int
    frontend_tool_id: Optional[int] = None
    backend_tool_id: Optional[int] = None
    database_id: Optional[int] = None
    cloud_id: Optional[int] = None


class UserSkillCreate(UserSkillBase):
    pass


class UserSkillRead(UserSkillBase):
    pass
