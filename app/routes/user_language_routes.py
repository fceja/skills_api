from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db

from app.models.user_model import User
from app.models.language_model import Language
from app.models.user_language_model import user_language

# init router
router = APIRouter()


# region - create operations
@router.post("/users/{user_id}/languages/{language_id}")
def add_language_to_user(user_id: int, language_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    language = db.query(Language).filter(Language.id == language_id).first()

    if not user or not language:
        raise HTTPException(status_code=404, detail="User or language not found.")

    exists = (
        db.query(user_language)
        .filter(
            user_language.c.user_id == user_id,
            user_language.c.language_id == language_id,
        )
        .first()
    )

    if exists:
        return {"success": True, "message": "Association already exists."}

    user.languages.append(language)
    db.commit()
    db.refresh(user)

    return {"success": True}


# endregion - create operations


# region - read operations
@router.get("/")
def get_user_language(start: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    results = db.query(user_language).offset(start).limit(limit).all()

    user_languages = [
        {"user_id": row.user_id, "language_id": row.language_id} for row in results
    ]

    return {"success": True, "user_languages": user_languages}


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
        user_language.select().where(
            user_language.c.user_id == user_id,
            user_language.c.language_id == language_id,
        )
    ).fetchone()

    if not exists:
        return {"success": True, "message": "Association does not exist."}

    user.languages.remove(language)
    db.commit()
    db.refresh(user)

    return {"success": True}


# endregion - delete operations
