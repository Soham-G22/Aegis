from datetime import datetime

from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Asset(Base):
    __tablename__ = "assets"

    id: Mapped[int] = mapped_column(primary_key=True)

    target_id: Mapped[int] = mapped_column(
        ForeignKey("targets.id"),
        nullable=False,
        index=True
    )

    hostname: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    asset_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    first_seen: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    last_seen: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    status: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default="active"
    )