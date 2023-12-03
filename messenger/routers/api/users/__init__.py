from fastapi import APIRouter

from .users import router as user_router

__all__ = ["user_router"]
