from fastapi import APIRouter
from app.models.store import Store
from app.services.store_services import create_store
store_router=APIRouter()

@store_router.post("/stores")
def create_store_api(store:Store):
    return create_store(store)