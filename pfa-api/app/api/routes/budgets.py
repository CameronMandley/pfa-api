from fastapi import APIRouter
from app.services.budgeting import compute_available_to_spend

router = APIRouter(prefix="/budgets", tags=["budgets"])

@router.get("/current")
async def get_current_budget():
    lines = [
        {"category":"Rent","planned":1300,"spent":1300},
        {"category":"Groceries","planned":400,"spent":220},
        {"category":"Dining","planned":250,"spent":190},
        {"category":"Transport","planned":200,"spent":80},
        {"category":"Savings","planned":500,"spent":500},
    ]
    ats = compute_available_to_spend(lines)
    return {"lines": lines, "available_to_spend": ats}
