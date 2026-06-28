from fastapi import FastAPI
from app.api.incident_router import incident_router
from app.api.store_router import store_router
from app.api.vendor_router import vendor_router
from app.ai.routers.ai_router import ai_router
from app.config.settings import settings
from app.database.database import create_tables
from app.database.models import stotre,incident,vendor



app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION
)
create_tables()
app.include_router(incident_router)
app.include_router(store_router)
app.include_router(vendor_router)
app.include_router(ai_router)

@app.get("/")
def home():
    return("AI Network Copilot is running")



