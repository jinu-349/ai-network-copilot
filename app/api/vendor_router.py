from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.vendor import Vendor
from app.services.vendor_service import create_vendor
from app.database.database import get_db

vendor_router = APIRouter()


@vendor_router.post("/vendors")
def create_vendor_api(
    vendor: Vendor,
    db: Session = Depends(get_db)
):
    return create_vendor(vendor, db)