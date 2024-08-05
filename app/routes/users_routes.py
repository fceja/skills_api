from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user_model import User
from app.models.language_model import Language
from app.schemas.user_schema import UserCreate

# init router
router = APIRouter()


# region - create operations
@router.post("/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(name=user.name, email=user.email)
    for id in user.language_ids:
        language = db.query(Language).filter(Language.id == id).first()
        if language:
            db_user.languages.append(language)

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


# region - update operations
@router.put("/{user_id}")
def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found.")

    db_user.name = user.name
    db_user.email = user.email

    db.commit()
    db.refresh(db_user)

    return {"success": True}


# endregion - update operations


# region - delete operations
@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found.")

    db.delete(db_user)
    db.commit()

    return {"success": True, "message": f"user_id {user_id} deleted."}


# endregion - delete operations
