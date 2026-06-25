from fastapi import FastAPI
from app.api.incident_router import incident_router

app=FastAPI()

app.include_router(incident_router)

@app.get("/")
def home():
    return("AI Network Copilot is running")



