from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.backend_tools_model import BackendTool
from app.schemas.backend_tool_schema import BackendToolCreate

router = APIRouter()


# region - create operations
@router.post("/")
def create_backend_tools(
    backend_tool_data: BackendToolCreate, db: Session = Depends(get_db)
):
    exists = (
        db.query(BackendTool).filter(BackendTool.name == backend_tool_data.name).first()
    )

    if exists:
        return {"success": True, "message": "Already exists."}

    db_backend_tool = BackendTool(backend_tool_data)

    db.add(db_backend_tool)
    db.commit()
    db.refresh(db_backend_tool)

    return {"success": True}


# endregion - create operations


# region - read operations
@router.get("/")
def get_backend_tools(start: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    backend_tools = db.query(BackendTool).offset(start).limit(limit).all()

    return {"success": True, "backend_tools": backend_tools}


# endregion - read operations
