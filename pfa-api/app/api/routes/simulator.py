from fastapi import APIRouter
from app.schemas.common import SimulatorRequest, SimulatorResponse
from app.services.simulator import simulate_purchase
from app.services.budgeting import compute_available_to_spend

router = APIRouter(prefix="/simulator", tags=["simulator"])

@router.post("/check", response_model=SimulatorResponse)
async def check(body: SimulatorRequest):
    ats = compute_available_to_spend([
        {"category":"Groceries","planned":400,"spent":220},
        {"category":"Dining","planned":250,"spent":190},
    ])
    impact, suggestions = simulate_purchase(body.price, body.category_hint, ats)
    return SimulatorResponse(impact=impact, suggestions=suggestions)
