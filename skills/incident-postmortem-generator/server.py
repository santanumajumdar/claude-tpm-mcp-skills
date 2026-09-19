from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from typing import List

app = FastAPI(title="Incident Postmortem Generator MCP")

class IncidentData(BaseModel):
    title: str
    raw_logs: str
    impact_duration_minutes: int

class PostmortemResponse(BaseModel):
    executive_summary: str
    timeline: List[str]
    action_items: List[str]

@app.post("/generate", response_model=PostmortemResponse)
async def generate_postmortem(data: IncidentData):
    """
    Generate a structured postmortem document from raw incident data.
    """
    if not data.raw_logs:
        raise HTTPException(status_code=400, detail="raw_logs cannot be empty")
        
    return PostmortemResponse(
        executive_summary=f"Incident {data.title} lasted for {data.impact_duration_minutes} minutes.",
        timeline=["Alert triggered", "Team paged", "Mitigation applied"],
        action_items=["Update runbook", "Add automated monitoring"]
    )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
