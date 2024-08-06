from fastapi import Depends
from sqlalchemy.orm import Session

from app.models.language_model import Language
from app.models.frontend_tools_model import FrontendTool
from app.models.user_model import User
from app.schemas.language_schema import LanguageCreate
from app.schemas.frontend_tool_schema import FrontendToolCreate
from app.schemas.user_schema import UserCreate


def seed_data(db: Session):
    if db.query(User).count() == 0:
        language1_data = UserCreate(name="fceja", email="fceja@email.com")
        language1 = User(language1_data)

        user2_data = UserCreate(name="jdoe", email="jdoe@email.com")
        user2 = User(user2_data)

        db.add_all([language1, user2])
        db.commit()

    if db.query(Language).count() == 0:
        language1_data = LanguageCreate(name="javascript")
        language1 = Language(language1_data)
        language2_data = LanguageCreate(name="typescript")
        language2 = Language(language2_data)
        language3_data = LanguageCreate(name="python")
        language3 = Language(language3_data)

        db.add_all([language1, language2, language3])
        db.commit()

    if db.query(FrontendTool).count() == 0:
        tool1_data = FrontendToolCreate(name="react")
        tool1 = FrontendTool(tool1_data)
        tool2_data = FrontendToolCreate(name="redux")
        tool2 = FrontendTool(tool2_data)
        tool3_data = FrontendToolCreate(name="fastapi")
        tool3 = FrontendTool(tool3_data)

        db.add_all([tool1, tool2, tool3])
        db.commit()
