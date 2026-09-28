from datetime import datetime

from pydantic import BaseModel


class AssetCreate(BaseModel):
    target_id: int
    hostname: str
    asset_type: str
    status: str = "active"


class AssetResponse(BaseModel):
    id: int
    target_id: int
    hostname: str
    asset_type: str
    first_seen: datetime
    last_seen: datetime
    status: str

    class Config:
        from_attributes = True