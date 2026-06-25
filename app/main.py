from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def home():
    return("AI Network Copilot is running")
