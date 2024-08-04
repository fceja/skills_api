from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.database import get_db
from api.models.user_model import User

router = APIRouter()


@router.get("/")
def get_user(start: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = db.query(User).offset(start).limit(limit).all()

    return {"success": True, "users": users}
