from sqlalchemy.orm import Session

from app.models.backend_tools_model import BackendTool
from app.models.frontend_tools_model import FrontendTool
from app.models.database_model import Database
from app.models.language_model import Language
from app.models.user_model import User
from app.models.user_skill_model import UserSkill
from app.schemas.backend_tool_schema import BackendToolCreate
from app.schemas.frontend_tool_schema import FrontendToolCreate
from app.schemas.database_schema import DatabaseCreate
from app.schemas.language_schema import LanguageCreate
from app.schemas.user_schema import UserCreate
from app.schemas.user_skill_schema import UserSkillCreate


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

        for user in ["react", "redux"]:
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

    if db.query(Database).count() == 0:
        databases = []

        for db_item in ["postgresql", "mysql", "microsoft sql server"]:
            database_data = DatabaseCreate(name=db_item)
            database = Database(database_data)
            databases.append(database)

        db.add_all(databases)
        db.commit()

    skills_data = {
        "user_id": 1,
        "language_id": 1,
        "database_id": 1,
        "backend_tool_id": 1,
        "frontend_tool_id": 2,
    }

    db_skills = UserSkillCreate(
        user_id=skills_data["user_id"],
        language_id=skills_data["language_id"],
        database_id=skills_data["database_id"],
        backend_tool_id=skills_data["backend_tool_id"],
        frontend_tool_id=skills_data["frontend_tool_id"],
    )
    db_skills = UserSkill(db_skills)
    db.add(db_skills)
    db.commit()
