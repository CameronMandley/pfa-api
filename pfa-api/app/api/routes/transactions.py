from fastapi import APIRouter
from app.jobs.tasks import sync_transactions_task

router = APIRouter(prefix="/transactions", tags=["transactions"])

@router.get("")
async def list_transactions(since: str | None = None):
    return {"transactions": []}

@router.post("/sync")
async def sync_now():
    res = sync_transactions_task.delay(1)
    return {"enqueued": True, "task_id": res.id}
