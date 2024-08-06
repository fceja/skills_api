from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.frontend_tools_model import FrontendTool
from app.schemas.frontend_tools_schema import FrontendToolsCreate

router = APIRouter()


# region - create operations
@router.post("/")
def get_frontend_tools(
    frontend_tool: FrontendToolsCreate, db: Session = Depends(get_db)
):
    exists = (
        db.query(FrontendTool).filter(FrontendTool.name == frontend_tool.name).first()
    )

    if exists:
        return {"success": True, "message": "Already exists."}

    db_frontend_tool = FrontendTool(name=frontend_tool.name)

    db.add(db_frontend_tool)
    db.commit()
    db.refresh(db_frontend_tool)

    return {"success": True}


# endregion - create operations


# region - read operations
@router.get("/")
def get_frontend_tools(start: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    frontend_tools = db.query(FrontendTool).offset(start).limit(limit).all()

    return {"success": True, "frontend_tools": frontend_tools}


# endregion - read operations
