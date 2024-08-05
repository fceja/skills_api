from fastapi import FastAPI

from api.database import engine
from api.models.base import Base
from api.routes import languages_routes, users_routes

# bind db models
Base.metadata.create_all(bind=engine)

# init api
api = FastAPI()

# add routes
api.include_router(languages_routes.router, prefix="/languages", tags=["languages"])
api.include_router(users_routes.router, prefix="/users", tags=["users"])


# root endpoint
@api.get("/")
def read_root():
    return {"message": "Root endpoint"}
