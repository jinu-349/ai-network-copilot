from sqlalchemy.orm import Session
from app.ai.prompts.incident_prompt import build_incident_prompt
from app.ai.client.openai_client import client

from app.database.models.incident import IncidentDB


def analyze_incident(
    incident_number: str,
    db: Session
):

    incident = db.query(
        IncidentDB
    ).filter(
        IncidentDB.incident_number == incident_number
    ).first()

    if incident is None:

        return {
            "message": "Incident not found"
        }
    prompt = build_incident_prompt(incident)

    response = client.responses.create(
        model="gpt-5.5",
        input=prompt
    )

    return {
        "incident_number": incident.incident_number,
        "analysis": response.output_text
    }