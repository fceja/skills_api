from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db

from app.models.backend_tools_model import BackendTool
from app.models.frontend_tools_model import FrontendTool
from app.models.database_model import Database
from app.models.cloud_model import Cloud
from app.models.language_model import Language
from app.models.user_model import User
from app.models.user_skill_model import UserSkill
from app.schemas.user_skill_schema import UserSkillCreate

# init router
router = APIRouter()


# region - create operations
@router.post("/")
def add_user_skills(user_skills: UserSkillCreate, db: Session = Depends(get_db)):
    db_user_skills = UserSkill(user_skills)
    db.add(db_user_skills)
    db.commit()
    db.refresh(db_user_skills)

    return {"success": True}


# endregion - create operations


# region - read operations
@router.get("/")
def get_user_skills(start: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    results = db.query(UserSkill).offset(start).limit(limit).all()

    return {"success": True, "user_skills": results}


@router.get("/users/{user_id}")
def get_user_skills_by_user_id(user_id: int, db: Session = Depends(get_db)):
    user = (
        db.query(User)
        .filter(User.id == user_id)
        .join(UserSkill, User.id == UserSkill.user_id)
        .outerjoin(Language, UserSkill.language_id == Language.id)
        .outerjoin(BackendTool, UserSkill.backend_tool_id == BackendTool.id)
        .outerjoin(FrontendTool, UserSkill.frontend_tool_id == FrontendTool.id)
        .outerjoin(Database, UserSkill.database_id == Database.id)
        .outerjoin(Cloud, UserSkill.cloud_id == Cloud.id)
        .first()
    )

    if not user:
        return {"success": False, "message": "User not found."}

    lang_results = [
        skill.language.name
        for skill in user.skills
        if skill.language and not skill.frontend_tool
    ]
    fe_results = [
        skill.frontend_tool.name for skill in user.skills if skill.frontend_tool
    ]
    be_results = [
        skill.backend_tool.name for skill in user.skills if skill.backend_tool
    ]
    db_results = [skill.database.name for skill in user.skills if skill.database]

    cloud_results = [skill.cloud.name for skill in user.skills if skill.cloud]

    return {
        "success": True,
        "user-skills": {
            "user": {
                "id": user_id,
                "name": user.name,
                "email": user.email,
            },
            "skills": {
                "languages": lang_results,
                "frontend_tools": fe_results,
                "backend_tools": be_results,
                "database": db_results,
                "cloud": cloud_results,
            },
        },
    }


# endregion - read operations


# region - delete operations
@router.delete("/users/{user_id}/languages/{language_id}")
def remove_language_from_user(
    user_id: int, language_id: int, db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.id == user_id).first()
    language = db.query(Language).filter(Language.id == language_id).first()

    if not user or not language:
        raise HTTPException(status_code=404, detail="User or language not found.")

    exists = db.execute(
        UserSkill.select().where(
            UserSkill.user_id == user_id,
            UserSkill.language_id == language_id,
        )
    ).fetchone()

    if not exists:
        return {"success": True, "message": "Association does not exist."}

    user.languages.remove(language)
    db.commit()
    db.refresh(user)

    return {"success": True}


# endregion - delete operations
