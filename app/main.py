from fastapi import FastAPI
from app.models.incident import Incident

app=FastAPI()

@app.get("/")
def home():
    return("AI Network Copilot is running")

@app.post("/incident")
def create_incident(incident:Incident):
    return{ "message": "Incident created successfully",
           "incident": incident}

