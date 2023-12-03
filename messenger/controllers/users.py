from .base import BaseController

from messenger.models import User
from messenger.repositories import UserRepo


class UserController(BaseController[User]):
    """
    User data controller.
    """
    def __init__(self, repository: UserRepo):
        super().__init__(model=User, repository=repository)
