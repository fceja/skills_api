from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.cloud_model import Cloud
from app.schemas.cloud_schema import CloudCreate

router = APIRouter()


# region - create operations
@router.post("/")
def create_cloud_tools(cloud_data: CloudCreate, db: Session = Depends(get_db)):
    exists = db.query(Cloud).filter(Cloud.name == cloud_data.name).first()

    if exists:
        return {"success": True, "message": "Already exists."}

    cloud = Cloud(cloud_data)

    db.add(cloud)
    db.commit()
    db.refresh(cloud)

    return {"success": True}


# endregion - create operations


# region - read operations
@router.get("/")
def get_clouds(start: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    clouds = db.query(Cloud).offset(start).limit(limit).all()

    return {"success": True, "cloud": clouds}


# endregion - read operations
