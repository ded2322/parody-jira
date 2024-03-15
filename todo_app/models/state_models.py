from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from todo_app.database import Base


class States(Base):
    __tablename__ = "states"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
