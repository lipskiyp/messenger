from fastapi import APIRouter

from .messages import messages_router
from .users import user_router

api_router = APIRouter()
api_router.include_router(
    messages_router,
    prefix="/messages",
)
api_router.include_router(
    user_router,
    prefix="/users",
)

__all__ = ["api_router"]
