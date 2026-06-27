from fastapi import FastAPI
from app.api.incident_router import incident_router
from app.api.store_router import store_router
from app.config.settings import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION
)

app.include_router(incident_router)
app.include_router(store_router)

@app.get("/")
def home():
    return("AI Network Copilot is running")



