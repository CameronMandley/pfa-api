from fastapi import APIRouter

router = APIRouter(prefix="/goals", tags=["goals"])

@router.post("")
async def create_goal(goal: dict):
    return {"ok": True, "goal": goal}

@router.get("")
async def list_goals():
    return {"goals": []}
