from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.target import Target
from app.schemas.target import TargetCreate, TargetResponse


router = APIRouter(
    prefix="/targets",
    tags=["Targets"]
)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=TargetResponse)
def create_target(
    target: TargetCreate,
    db: Session = Depends(get_db)
):
    new_target = Target(
        name=target.name,
        domain=target.domain,
        is_authorized=target.is_authorized
    )

    db.add(new_target)
    db.commit()
    db.refresh(new_target)

    return new_target