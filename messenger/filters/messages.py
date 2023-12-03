"""
FastAPI filters for messages.
"""

from datetime import datetime
from fastapi_filter.contrib.sqlalchemy import Filter
from typing import Optional

from messenger.models import Message


class MessageFilter(Filter):
    """
    FastAPI messages filters.
    """
    sender: Optional[int] = None
    receiver: Optional[int] = None
    created_at: Optional[int] = None
    order_by: Optional[str] = None

    class Constants(Filter.Constants):
        model = Message
