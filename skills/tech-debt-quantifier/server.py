from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from typing import List

app = FastAPI(title="Tech Debt Quantifier MCP")

class DebtItem(BaseModel):
    component: str
    debt_type: str  # e.g., "code_smell", "missing_tests", "legacy_dependency"
    severity: str

class QuantifiedDebt(BaseModel):
    estimated_hours_lost_per_month: int
    risk_level: str
    executive_summary: str

@app.post("/quantify", response_model=QuantifiedDebt)
async def quantify_debt(items: List[DebtItem]):
    """
    Quantify the business impact of technical debt.
    """
    hours = len(items) * 5  # Simple heuristic for demonstration
    risk = "High" if any(i.severity == "Critical" for i in items) else "Medium"
    
    return QuantifiedDebt(
        estimated_hours_lost_per_month=hours,
        risk_level=risk,
        executive_summary=f"We have {len(items)} major technical debt items costing us ~{hours} hours of lost productivity per month."
    )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
