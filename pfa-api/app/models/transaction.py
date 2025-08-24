from sqlalchemy import ForeignKey, String, Numeric, Date
from sqlalchemy.orm import Mapped, mapped_column
from app.db.session import Base

class Transaction(Base):
    __tablename__ = "transactions"
    id: Mapped[int] = mapped_column(primary_key=True)
    account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id", ondelete="CASCADE"), index=True)
    date: Mapped[str] = mapped_column(Date, index=True)
    amount: Mapped[float] = mapped_column(Numeric(14,2))
    merchant: Mapped[str] = mapped_column(String(256))
    category: Mapped[str] = mapped_column(String(64), index=True)
    raw_json: Mapped[str] = mapped_column(String)
