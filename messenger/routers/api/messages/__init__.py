from fastapi import APIRouter

from .messages import router as messages_router

__all__ = ["messages_router"]
