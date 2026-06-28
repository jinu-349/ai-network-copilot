from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.database import Base


class VendorDB(Base):
    __tablename__ = "vendors"

    vendor_id: Mapped[str] = mapped_column(
        String(20),
        primary_key=True
    )

    vendor_name: Mapped[str] = mapped_column(
        String(100)
    )

    vendor_email: Mapped[str] = mapped_column(
        String(100)
    )

    vendor_phone: Mapped[str] = mapped_column(
        String(20)
    )

    vendor_type: Mapped[str] = mapped_column(
        String(50)
    )

    supported_states: Mapped[str] = mapped_column(
        String(200)
    )