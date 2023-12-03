"""
Pydantic validation schemas for users.
"""

from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from uuid import UUID


class UserResponseSchema(BaseModel):
    """
    Pydantic user schema for server reponses.
    """
    id: UUID
    username: str
    firstname: str
    surname: str
    created_at: datetime
    updated_at: datetime


class UserCreateSchema(BaseModel):
    """
    Pydantic user schema for create requests.
    """
    username: str
    firstname: str
    surname: str


class UserUpdateSchema(BaseModel):
    """
    Pydantic user schema for update requests.
    """
    username: Optional[str] = None
    firstname: Optional[str] = None
    surname: Optional[str] = None
