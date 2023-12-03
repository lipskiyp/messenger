"""
FastAPI endpoints for messages.
"""

from fastapi import APIRouter, Depends, status
from fastapi_filter import FilterDepends
from typing import List
from uuid import UUID

from messenger.controllers import MessageController
from messenger.factories import ControllerFactory
from messenger.filters import MessageFilter
from messenger.schemas import (
    MessagesCreateSchema,
    MessagesResponseSchema,
    MessagesUpdateSchema,
)


router = APIRouter()


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
)
async def create_message(
    request: MessagesCreateSchema,
    controller: MessageController = Depends(ControllerFactory().get_message_controller),
) -> MessagesResponseSchema:
    """
    Create a message.
    """
    return await controller.create(request=request)

@router.get("/")
async def list_messages(
    controller: MessageController = Depends(ControllerFactory().get_message_controller),
    filters: MessageFilter = FilterDepends(MessageFilter),
) -> List[MessagesResponseSchema]:
    """
    List all messagea.
    """
    return await controller.list(filters=filters)


@router.get("/{id}")
async def get_message(
    id: UUID,
    controller: MessageController = Depends(ControllerFactory().get_message_controller),
) -> MessagesResponseSchema:
    """
    Get a message by uuid.
    """
    return await controller.get_by_id(_id=id)


@router.patch(
    "/{id}",
    status_code=status.HTTP_201_CREATED,
)
async def update_message(
    id: UUID,
    request: MessagesUpdateSchema,
    controller: MessageController = Depends(ControllerFactory().get_message_controller),
) -> MessagesResponseSchema:
    """
    Update a message by uuid.
    """
    return await controller.update_by_id(_id=id, request=request)


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_message(
    id: UUID,
    controller: MessageController = Depends(ControllerFactory().get_message_controller),
):
    """
    Delete a message by uuid.
    """
    return await controller.delete_by_id(_id=id)
