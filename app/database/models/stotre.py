from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship

from app.database.database import Base

class StoreDB(Base):
    __tablename__ = "stores"
    incidents = relationship(
    "IncidentDB",
    back_populates="store"
)

    store_id: Mapped[str] = mapped_column(
        String(20),
        primary_key=True
    )

    store_name: Mapped[str] = mapped_column(String(100))

    address: Mapped[str] = mapped_column(String(200))

    city: Mapped[str] = mapped_column(String(50))

    state: Mapped[str] = mapped_column(String(50))

    zip_code: Mapped[str] = mapped_column(String(20))

    contact_name: Mapped[str] = mapped_column(String(100))

    contact_email: Mapped[str] = mapped_column(String(100))

    contact_number: Mapped[str] = mapped_column(String(20))
