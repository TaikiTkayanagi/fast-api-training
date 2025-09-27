from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy import ForeignKey, Integer, String, DateTime, text
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship


class Base(AsyncAttrs, DeclarativeBase):
    pass

class Memo(Base):
    __tablename__ = 'memos'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    content: Mapped[str] = mapped_column(String(300), nullable=False)
    status_id: Mapped[int] = mapped_column(Integer, ForeignKey("status.id"), nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime, nullable=False, server_default=text("datetime('now','localtime')"))
    updated_at: Mapped[DateTime] = mapped_column(DateTime, nullable=False, server_default=text("datetime('now','localtime')"), onupdate=text("datetime('now','localtime')"))

    status = relationship("Status")
