from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.store import Store
from app.services.store_service import create_store
from app.database.database import get_db

store_router = APIRouter()


@store_router.post("/stores")
def create_store_api(
    store: Store,
    db: Session = Depends(get_db)
):
    return create_store(store, db)