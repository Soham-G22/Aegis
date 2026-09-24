from fastapi import FastAPI

from app.models.asset import Asset

# from app.database import Base, engine
from app.models.target import Target
from app.api.targets import router as target_router


# Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Aegis API",
    description="Attack Surface Intelligence Platform",
    version="0.1.0"
)


app.include_router(target_router)


@app.get("/")
def root():
    return {
        "project": "Aegis",
        "status": "running",
        "version": "0.1.0"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }