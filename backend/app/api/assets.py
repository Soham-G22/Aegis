from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.asset import Asset
from app.schemas.asset import AssetCreate, AssetResponse
from app.models.target import Target


router = APIRouter(
    prefix="/assets",
    tags=["Assets"]
)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=AssetResponse)

def create_asset(
    
    asset: AssetCreate,
    db: Session = Depends(get_db)
):
    target = db.query(Target).filter(
    Target.id == asset.target_id
).first()

    if target is None:
        raise HTTPException(
            status_code=404,
            detail="Target not found"
        )
    
    new_asset = Asset(
        target_id=asset.target_id,
        hostname=asset.hostname,
        asset_type=asset.asset_type,
        status=asset.status
    )

@router.get("/", response_model=list[AssetResponse])
def get_assets(
    db: Session = Depends(get_db)
):
    assets = db.query(Asset).all()

    return assets
    

    db.add(new_asset)
    db.commit()
    db.refresh(new_asset)

    return new_asset