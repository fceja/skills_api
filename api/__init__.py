from fastapi import FastAPI

from api.routes import languages_routes, users_routes

# init api
api = FastAPI()

# add routes
api.include_router(languages_routes.router, prefix="/languages", tags=["languages"])
api.include_router(users_routes.router, prefix="/users", tags=["users"])


# root endpoint
@api.get("/")
def read_root():
    return {"message": "Root endpoint"}
