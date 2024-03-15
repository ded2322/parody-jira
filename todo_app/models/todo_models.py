from sqlalchemy import String, ForeignKey, Column, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from todo_app.database import Base

class Tasks(Base):
    __tablename__ = "tasks"

    id:Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    title: Mapped[str] = mapped_column(String(length=100))
    description: Mapped[str]
    created_at = Column(DateTime, default=lambda: datetime.utcnow())
    state: Mapped[int] = mapped_column(ForeignKey("states.id",ondelete="CASCADE"))