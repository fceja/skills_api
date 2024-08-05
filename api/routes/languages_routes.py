from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.database import get_db
from api.models.language_model import Language
from api.schemas.language_schema import LanguageCreate

# init router
router = APIRouter()


# region - create operations
@router.post("/")
def create_languages(language: LanguageCreate, db: Session = Depends(get_db)):
    db_language = Language(name=language.name)
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
