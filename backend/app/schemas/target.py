from pydantic import BaseModel


class TargetCreate(BaseModel):
    name: str
    domain: str
    is_authorized: bool = False


class TargetResponse(BaseModel):
    id: int
    name: str
    domain: str
    is_authorized: bool

    class Config:
        from_attributes = True