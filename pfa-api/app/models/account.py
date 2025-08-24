from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from app.db.session import Base

class Account(Base):
    __tablename__ = "accounts"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), index=True)
    provider: Mapped[str] = mapped_column(String(50))
    mask: Mapped[str] = mapped_column(String(8))
    name: Mapped[str] = mapped_column(String(120))
    item_id: Mapped[str] = mapped_column(String(128))
    access_token_enc: Mapped[str] = mapped_column(String(512))
