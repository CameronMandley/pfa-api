import os
from functools import lru_cache

class Settings:
    API_HOST: str = os.getenv("API_HOST", "0.0.0.0")
    API_PORT: int = int(os.getenv("API_PORT", "8000"))
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql+asyncpg://postgres:postgres@localhost:5432/pfa")
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    PLAID_ENV: str = os.getenv("PLAID_ENV", "sandbox")
    PLAID_CLIENT_ID: str = os.getenv("PLAID_CLIENT_ID", "")
    PLAID_SECRET: str = os.getenv("PLAID_SECRET", "")

@lru_cache
def get_settings() -> Settings:
    return Settings()
