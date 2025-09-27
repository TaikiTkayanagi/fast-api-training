from sqlalchemy import DateTime, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from model.memo import Base


class Status(Base):
    __tablename__ = 'status'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    deadline: Mapped[DateTime | None] = mapped_column(DateTime, nullable=True)
    is_complete: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)