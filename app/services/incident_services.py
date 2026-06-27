from app.models.incident import Incident


def create_incident(incident: Incident):
    return {
        "message": "Incident created successfully",
        "incident": incident
    }