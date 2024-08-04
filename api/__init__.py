from fastapi import FastAPI

from api.models.user_model import Base
from api.routes import users_routes
from api.database import engine

Base.metadata.create_all(bind=engine)

api = FastAPI()

api.include_router(users_routes.router, prefix="/users", tags=["users"])


@api.get("/")
def read_root():
    return {"message": "Root endpoint"}
