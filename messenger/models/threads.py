"""
Threads SQLAlchemy ORM model.
"""

from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid import UUID as uuid

from .base import CommonBase


class Thread(CommonBase):
    """
    Threads ORM model.
    """
    __tablename__ = "threads"

    user1_id: Mapped[uuid] = mapped_column(
        UUID,
        ForeignKey("users.id", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
        nullable=False,
    )
    user1: Mapped["User"] = relationship(
        backref="threads",
        foreign_keys=[user1_id],
        init=False,
    )

    user2_id: Mapped[uuid] = mapped_column(
        UUID,
        ForeignKey("users.id", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
        nullable=False,
    )
    user2: Mapped["User"] = relationship(
        #backref="threads",
        foreign_keys=[user2_id],
        init=False,
    )

    __mapper_args__ = {
        'eager_defaults': True,
    }
