from pydantic import BaseModel

class Health(BaseModel):
    status: str = "ok"

class LinkToken(BaseModel):
    link_token: str

class PublicToken(BaseModel):
    public_token: str

class SimulatorRequest(BaseModel):
    price: float
    merchant: str
    category_hint: str | None = None

class SimulatorResponse(BaseModel):
    impact: str
    suggestions: list[str] = []
