"""
User data repository.
"""

from sqlalchemy.ext.asyncio import AsyncSession

from messenger.models import User
from .base import BaseRepo


class UserRepo(BaseRepo[User]):
    """
    User data repository.
    """
    def __init__(self, db_session: AsyncSession, model: User):
        super().__init__(db_session=db_session, model=model)
