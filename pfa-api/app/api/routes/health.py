from fastapi import APIRouter
from app.schemas.common import Health

router = APIRouter()

@router.get("/health", response_model=Health)
async def health():
    return Health()
