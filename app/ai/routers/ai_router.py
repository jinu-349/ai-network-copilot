from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.ai import AIIncidentRequest
from app.ai.services.ai_service import analyze_incident
from app.database.database import get_db

ai_router = APIRouter()


@ai_router.post("/ai/analyze-incident")
def analyze_incident_api(
    request: AIIncidentRequest,
    db: Session = Depends(get_db)
):
    return analyze_incident(
        request.incident_number,
        db
    )