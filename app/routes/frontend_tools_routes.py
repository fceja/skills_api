from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.frontend_tools_model import FrontendTool
from app.schemas.frontend_tool_schema import FrontendToolCreate

router = APIRouter()


# region - create operations
@router.post("/")
def create_frontend_tools(
    frontend_tool_data: FrontendToolCreate, db: Session = Depends(get_db)
):
    exists = (
        db.query(FrontendTool)
        .filter(FrontendTool.name == frontend_tool_data.name)
        .first()
    )

    if exists:
        return {"success": True, "message": "Already exists."}

    db_frontend_tool = FrontendTool(frontend_tool_data)

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
