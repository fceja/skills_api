from sqlalchemy.orm import Session

from app.models.backend_tools_model import BackendTool
from app.models.frontend_tools_model import FrontendTool
from app.models.language_model import Language
from app.models.user_model import User
from app.schemas.backend_tool_schema import BackendToolCreate
from app.schemas.frontend_tool_schema import FrontendToolCreate
from app.schemas.language_schema import LanguageCreate
from app.schemas.user_schema import UserCreate


def seed_data(db: Session):
    if db.query(User).count() == 0:
        users = []

        users_to_create = [
            {"name": "fceja", "email": "fceja.dev@email.com"},
            {"name": "jdoe", "email": "jdoe@email.com"},
        ]

        for user in users_to_create:
            user_data = UserCreate(name=user["name"], email=user["email"])
            users.append(User(user_data))

        db.add_all(users)
        db.commit()

    if db.query(Language).count() == 0:
        languages = []

        for user in ["javascript", "typescript", "python", "go"]:
            lang_data = LanguageCreate(name=user)
            lang = Language(lang_data)
            languages.append(lang)

        db.add_all(languages)
        db.commit()

    if db.query(FrontendTool).count() == 0:
        frontend_tools = []

        for user in ["react", "redux", "fastapi"]:
            fe_tool_data = FrontendToolCreate(name=user)
            fe_tool = FrontendTool(fe_tool_data)
            frontend_tools.append(fe_tool)

        db.add_all(frontend_tools)
        db.commit()

    if db.query(BackendTool).count() == 0:
        backend_tools = []

        for user in ["fastapi", "node", "express"]:
            be_tool_data = BackendToolCreate(name=user)
            be_tool = BackendTool(be_tool_data)
            backend_tools.append(be_tool)

        db.add_all(backend_tools)
        db.commit()
