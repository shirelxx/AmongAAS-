import datetime
import enum
import uuid

from sqlalchemy import String, DateTime, Enum
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


class Base(DeclarativeBase):
    pass


class Status(enum.Enum):
    CREATED = 'CREATED'
    DELETED = 'DELETED'


class Deployments(Base):
    __tablename__ = "deployment"

    id: Mapped[uuid.UUID] = mapped_column(default=uuid.uuid4, primary_key=True)
    db_name: Mapped[str] = mapped_column(String(40))
    status: Mapped[Enum] = mapped_column(Enum(Status))
    username: Mapped[str] = mapped_column(String(40))
    creation_time: Mapped[datetime.datetime] = mapped_column(DateTime)

