from fastapi import APIRouter
from app.models.incident import Incident

incident_router=APIRouter()

@incident_router.post("/incident")
def create_incident(incident:Incident):
    return{ "message": "Incident created successfully",
           "incident": incident}

