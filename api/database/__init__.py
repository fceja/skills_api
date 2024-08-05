from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from api.models.base import Base
from api.models import user_model, language_model, user_language_model

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
