from sqlalchemy import ForeignKey, String, Numeric, Date
from sqlalchemy.orm import Mapped, mapped_column
from app.db.session import Base

class Budget(Base):
    __tablename__ = "budgets"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    period_start: Mapped[str] = mapped_column(Date)
    period_end: Mapped[str] = mapped_column(Date)

class BudgetLine(Base):
    __tablename__ = "budget_lines"
    id: Mapped[int] = mapped_column(primary_key=True)
    budget_id: Mapped[int] = mapped_column(ForeignKey("budgets.id", ondelete="CASCADE"), index=True)
    category: Mapped[str] = mapped_column(String(64), index=True)
    planned: Mapped[float] = mapped_column(Numeric(14,2))
    spent: Mapped[float] = mapped_column(Numeric(14,2), default=0)
