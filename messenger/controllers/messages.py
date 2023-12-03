from .base import BaseController

from messenger.models import Message
from messenger.repositories import MessagesRepo


class MessageController(BaseController[Message]):
    """
    Messages data controller.
    """
    def __init__(self, repository: MessagesRepo):
        super().__init__(model=Message, repository=repository)
