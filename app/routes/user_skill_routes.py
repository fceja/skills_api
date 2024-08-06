from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db

from app.models.user_model import User
from app.models.language_model import Language
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
