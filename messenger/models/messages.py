"""
Message SQLAlchemy ORM model.
"""

from sqlalchemy import String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid import UUID as uuid

from .base import CommonBase


class Message(CommonBase):
    """
    Messages ORM model.
    """
    __tablename__ = "messages"

    sender_id: Mapped[uuid] = mapped_column(
        UUID,
        ForeignKey("users.id", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
        nullable=False,
    )
    sender: Mapped["User"] = relationship(
        backref="sent_messages",
        foreign_keys=[sender_id],
        init=False,
    )

    receiver_id: Mapped[uuid] = mapped_column(
        UUID,
        ForeignKey("users.id", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
        nullable=False
    )
    receiver: Mapped["User"] = relationship(
        backref="received_messages",
        foreign_keys=[receiver_id],
        init=False,
    )

    text: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )


    __mapper_args__ = {
        'eager_defaults': True,
    }
