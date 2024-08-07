from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.database_model import Database
from app.schemas.database_schema import DatabaseCreate

router = APIRouter()


# region - create operations
@router.post("/")
def create_database(database_data: DatabaseCreate, db: Session = Depends(get_db)):
    exists = db.query(Database).filter(Database.name == database_data.name).first()

    if exists:
        return {"success": True, "message": "Already exists."}

    database = Database(database_data)

    db.add(database)
    db.commit()
    db.refresh(database)

    return {"success": True}


# endregion - create operations


# region - read operations
@router.get("/")
def get_databases(start: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    databases = db.query(Database).offset(start).limit(limit).all()

    return {"success": True, "databases": databases}


# endregion - read operations
