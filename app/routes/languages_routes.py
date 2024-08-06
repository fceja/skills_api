from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.language_model import Language
from app.schemas.language_schema import LanguageCreate

# init router
router = APIRouter()


# region - create operations
@router.post("/")
def create_languages(language_data: LanguageCreate, db: Session = Depends(get_db)):
    db_language = Language(language_data)
    db.add(db_language)
    db.commit()
    db.refresh(db_language)

    return {"success": True}


# endregion - create operations


# region - read operations
@router.get("/")
def get_languages(start: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    languages = db.query(Language).offset(start).limit(limit).all()

    return {"success": True, "languages": languages}


# endregion - read operations
