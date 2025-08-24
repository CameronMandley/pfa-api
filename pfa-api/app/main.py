from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes.health import router as health_router
from app.api.routes.plaid import router as plaid_router
from app.api.routes.transactions import router as transactions_router
from app.api.routes.budgets import router as budgets_router
from app.api.routes.goals import router as goals_router
from app.api.routes.simulator import router as simulator_router

app = FastAPI(title="PFA API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
app.include_router(plaid_router)
app.include_router(transactions_router)
app.include_router(budgets_router)
app.include_router(goals_router)
app.include_router(simulator_router)
