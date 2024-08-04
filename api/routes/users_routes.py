from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.database import get_db
from api.models.user_model import User
from api.schemas.user_schema import UserCreate, UserRead

router = APIRouter()


# region - create operations
@router.post("/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return {"success": True}


# endregion - create operations


# region - read operations
@router.get("/")
def get_user(start: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = db.query(User).offset(start).limit(limit).all()

    return {"success": True, "users": users}


# endregion - read operations
