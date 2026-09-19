from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from typing import List, Dict

app = FastAPI(title="Sprint Spillover Analyzer MCP")

class Ticket(BaseModel):
    ticket_id: str
    title: str
    sprints_active: int
    story_points: int

class AnalysisResponse(BaseModel):
    total_spillover_points: int
    chronic_spillover_tickets: List[str]
    recommendations: str

@app.post("/analyze", response_model=AnalysisResponse)
async def analyze_spillover(tickets: List[Ticket]):
    """
    Analyze sprint spillover metrics.
    """
    spillover_points = sum(t.story_points for t in tickets)
    chronic = [t.ticket_id for t in tickets if t.sprints_active > 1]
    
    return AnalysisResponse(
        total_spillover_points=spillover_points,
        chronic_spillover_tickets=chronic,
        recommendations="Break down chronic tickets into smaller stories."
    )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
