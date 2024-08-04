from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.database import get_db

router = APIRouter()


@router.get("/")
def get_user(db: Session = Depends(get_db)):
    print(f"/user db -> {db}")

    return {"message": "/users - get_users "}
