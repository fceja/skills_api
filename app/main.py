from fastapi import FastAPI
import uvicorn

from app.routes import languages_routes, users_routes

# init app
app = FastAPI()

# add routes
app.include_router(languages_routes.router, prefix="/languages", tags=["languages"])
app.include_router(users_routes.router, prefix="/users", tags=["users"])


# main entry
if __name__ == "__main__":
    uvicorn.run(app)
