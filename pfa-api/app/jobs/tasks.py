from app.jobs.celery_app import celery_app

@celery_app.task
def sync_transactions_task(user_id: int) -> dict:
    return {"status": "ok", "user_id": user_id, "synced": 42}
