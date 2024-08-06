from fastapi import FastAPI
import uvicorn

from app.routes import (
    languages_routes,
    frontend_tools_routes,
    users_routes,
    user_language_routes,
)

# init app
app = FastAPI()

# add routes
app.include_router(languages_routes.router, prefix="/languages", tags=["languages"])
app.include_router(
    frontend_tools_routes.router, prefix="/frontend-tools", tags=["frontend-tools"]
)
app.include_router(users_routes.router, prefix="/users", tags=["users"])
app.include_router(
    user_language_routes.router, prefix="/user-languages", tags=["user-languages"]
)


# main entry
if __name__ == "__main__":
    uvicorn.run(app)
