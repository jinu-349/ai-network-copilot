from sqlalchemy.orm import Session

from app.schemas.vendor import Vendor
from app.database.models.vendor import VendorDB


def create_vendor(vendor: Vendor, db: Session):

    db_vendor = VendorDB(
        vendor_id=vendor.vendor_id,
        vendor_name=vendor.vendor_name,
        vendor_email=vendor.vendor_email,
        vendor_phone=vendor.vendor_phone,
        vendor_type=vendor.vendor_type,
        supported_states=vendor.supported_states
    )

    db.add(db_vendor)
    db.commit()
    db.refresh(db_vendor)

    return {
        "message": "Vendor created successfully",
        "vendor": db_vendor
    }