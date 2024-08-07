from fastapi import FastAPI
import uvicorn

from app.routes import (
    languages_routes,
    cloud_routes,
    database_routes,
    frontend_tools_routes,
    backend_tools_routes,
    user_skill_routes,
    users_routes,
)

# init app
app = FastAPI()

# add routes
app.include_router(languages_routes.router, prefix="/languages", tags=["languages"])
app.include_router(cloud_routes.router, prefix="/clouds", tags=["clouds"])
app.include_router(database_routes.router, prefix="/databases", tags=["databases"])
app.include_router(
    backend_tools_routes.router, prefix="/backend-tools", tags=["backend-tools"]
)
app.include_router(
    frontend_tools_routes.router, prefix="/frontend-tools", tags=["frontend-tools"]
)
app.include_router(users_routes.router, prefix="/users", tags=["users"])
app.include_router(
    user_skill_routes.router, prefix="/user-skills", tags=["user-skills"]
)


# main entry
if __name__ == "__main__":
    uvicorn.run(app)
