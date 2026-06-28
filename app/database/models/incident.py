from sqlalchemy import String, Text, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from app.database.database import Base

#git test
class IncidentDB(Base):
    __tablename__ = "incidents"

    store = relationship(
    "StoreDB",
    back_populates="incidents"
)

    incident_number: Mapped[str] = mapped_column(
        String(20),
        primary_key=True
    )

    store_id: Mapped[str] = mapped_column(
    ForeignKey("stores.store_id")
)

    caller: Mapped[str] = mapped_column(
        String(100)
    )

    short_description: Mapped[str] = mapped_column(
        String(255)
    )

    description: Mapped[str] = mapped_column(
        Text
    )

    work_notes: Mapped[str] = mapped_column(
        Text,
        nullable=True
    )

    priority: Mapped[str] = mapped_column(
        String(10)
    )

    status: Mapped[str] = mapped_column(
        String(20),
        default="New"
    )

    assignment_group: Mapped[str] = mapped_column(
        String(100)
    )

    assigned_to: Mapped[str] = mapped_column(
        String(100)
    )

    created_at: Mapped[DateTime] = mapped_column(
        DateTime,
        server_default=func.now()
    )

    updated_at: Mapped[DateTime] = mapped_column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now()
    )