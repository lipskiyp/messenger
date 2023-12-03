"""
Messages data repository.
"""

from sqlalchemy.ext.asyncio import AsyncSession

from messenger.models import Message
from .base import BaseRepo


class MessagesRepo(BaseRepo[Message]):
    """
    Messages data repository.
    """
    def __init__(self, db_session: AsyncSession, model: Message):
        super().__init__(db_session=db_session, model=model)
