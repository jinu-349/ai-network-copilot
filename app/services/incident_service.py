from sqlalchemy.orm import Session

from app.schemas.incident import Incident
from app.database.models.incident import IncidentDB


def create_incident(incident: Incident, db: Session):

    db_incident = IncidentDB(
        incident_number=incident.incident_number,
        store_id=incident.store_id,
        caller=incident.caller,
        short_description=incident.short_description,
        description=incident.description,
        work_notes=incident.work_notes,
        priority=incident.priority,
        assignment_group=incident.assignment_group,
        assigned_to=incident.assigned_to
    )

    db.add(db_incident)

    db.commit()

    db.refresh(db_incident)

    return {
        "message": "Incident created successfully",
        "incident": db_incident
    }