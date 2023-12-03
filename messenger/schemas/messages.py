"""
Pydantic validation schemas for messages.
"""

from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from uuid import UUID


class MessagesResponseSchema(BaseModel):
    """
    Pydantic messages schema for server reponses.
    """
    id: UUID
    sender_id: UUID
    receiver_id: UUID
    text: str
    created_at: datetime
    updated_at: datetime


class MessagesCreateSchema(BaseModel):
    """
    Pydantic messages schema for create requests.
    """
    sender_id: UUID
    receiver_id: UUID
    text: str


class MessagesUpdateSchema(BaseModel):
    """
    Pydantic messages schema for update requests.
    """
    sender_id: Optional[UUID] = None
    receiver_id: Optional[UUID] = None
    text: Optional[str] = None
