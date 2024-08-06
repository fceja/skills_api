from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models import (
    user_model,
    language_model,
    frontend_tools_model,
    user_skill_model,
)

from app.models.base import Base

# init db
DATABASE_URL = "sqlite:///./skills.db"
CONNECT_ARGS = {"check_same_thread": False}

engine = create_engine(DATABASE_URL, connect_args=CONNECT_ARGS)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()
