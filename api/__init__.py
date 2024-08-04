from fastapi import FastAPI

from api.routes import users

api = FastAPI()

api.include_router(users.router, prefix="/users", tags=["users"])


@api.get("/")
def read_root():
    return {"message": "Root endpoint"}
