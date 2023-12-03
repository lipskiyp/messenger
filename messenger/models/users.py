"""
User SQLAlchemy ORM model.
"""

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

from .base import CommonBase



class User(CommonBase):
    """
    Users ORM model.
    """
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(
        String(64),
        unique=True,
        index=True,
        nullable=False,
    )
    firstname: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
    )
    surname: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
    )

    __mapper_args__ = {
        'eager_defaults': True,
    }
