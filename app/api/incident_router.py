from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.models.incident import Incident
from app.services.incident_services import create_incident
from app.database.database import get_db

incident_router = APIRouter()


@incident_router.post("/incident")
def create_incident_api(
    incident: Incident,
    db: Session = Depends(get_db)
):
    return create_incident(incident, db)
