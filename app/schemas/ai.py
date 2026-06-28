from pydantic import BaseModel


class AIIncidentRequest(BaseModel):
    incident_number: str