from fastapi import APIRouter
from app.models.incident import Incident
from app.services.incident_services import create_incident

incident_router=APIRouter()

@incident_router.post("/incident")
def create_incident_api(incident:Incident):
    return create_incident(incident)

