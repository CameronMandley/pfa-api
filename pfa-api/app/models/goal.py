from sqlalchemy import ForeignKey, String, Numeric, Date
from sqlalchemy.orm import Mapped, mapped_column
from app.db.session import Base

class Goal(Base):
    __tablename__ = "goals"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), index=True)
    name: Mapped[str] = mapped_column(String(120))
    target_amount: Mapped[float] = mapped_column(Numeric(14,2))
    target_date: Mapped[str] = mapped_column(Date)
    start_balance: Mapped[float] = mapped_column(Numeric(14,2), default=0)
    cadence: Mapped[str] = mapped_column(String(16), default="monthly")
