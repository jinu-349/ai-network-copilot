from pydantic import BaseModel

class Incident(BaseModel):
    incident_number: str
    caller : str
    short_description: str
    description: str
    work_notes: str
    priority: str
    assignment_group:str
    assigned_to: str