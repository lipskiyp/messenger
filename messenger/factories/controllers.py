"""
Database controller factory.
"""

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from messenger.database import get_session
from messenger.controllers import (
    UserController,
    MessageController
)
from messenger.models import (
    User,
    Message
)
from messenger.repositories import (
    UserRepo,
    MessagesRepo
)


class ControllerFactory:
    """
    Database controller factory.
    """
    def get_user_controller(self, db_session: AsyncSession = Depends(get_session)):
        """
        Returns User database controller.
        """
        return UserController(
            repository=UserRepo(
                db_session=db_session,
                model=User,
            )
        )

    def get_message_controller(self, db_session: AsyncSession = Depends(get_session)):
        """
        Returns Message database controller.
        """
        return MessageController(
            repository=MessagesRepo(
                db_session=db_session,
                model=Message,
            )
        )
