"""
Base SQLAlchemy ORM model.
"""

from datetime import datetime
from sqlalchemy import DateTime, Table, ForeignKey, Column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, MappedAsDataclass
from sqlalchemy.sql import func
from uuid import UUID as uuid
from uuid import uuid4


class Base(MappedAsDataclass, DeclarativeBase):
    pass


class CommonBase(Base):
    """
    Base ORM model.
    """
    __tablename__ = 'common_base'
    __abstract__ = True

    id: Mapped[uuid] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
        nullable=False,
        init=False,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        init=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        init=False,
    )
