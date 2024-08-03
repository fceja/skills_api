from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from api.database import get_db

api = FastAPI()


@api.get("/")
def read_root():
    return {"message": "Root endpoint"}


@api.get("/testdb")
def read_root_2(db: Session = Depends(get_db)):
    print(f"test db -> {db}")
