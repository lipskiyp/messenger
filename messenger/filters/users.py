"""
FastAPI filters for users.
"""

from datetime import datetime
from fastapi_filter.contrib.sqlalchemy import Filter
from typing import Optional

from messenger.models import User


class UserFilter(Filter):
    """
    FastAPI users filters.
    """
    created_at: Optional[int] = None
    order_by: Optional[str] = None

    class Constants(Filter.Constants):
        model = User
