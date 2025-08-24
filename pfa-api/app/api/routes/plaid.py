from fastapi import APIRouter
from app.schemas.common import LinkToken, PublicToken
from app.services import plaid as plaid_svc

router = APIRouter(prefix="/plaid", tags=["plaid"])

@router.post("/link_token", response_model=LinkToken)
async def link_token():
    token = plaid_svc.create_link_token("demo-user")
    return LinkToken(**token)

@router.post("/exchange")
async def exchange(body: PublicToken):
    data = plaid_svc.exchange_public_token(body.public_token)
    return data

@router.post("/webhook")
async def webhook(payload: dict):
    return {"ok": True}
