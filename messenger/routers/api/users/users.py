"""
FastAPI endpoints for users.
"""

from fastapi import APIRouter, Depends, status
from fastapi_filter import FilterDepends
from typing import List
from uuid import UUID

from messenger.controllers import UserController
from messenger.factories import ControllerFactory
from messenger.filters import UserFilter
from messenger.schemas import (
    UserResponseSchema,
    UserCreateSchema,
    UserUpdateSchema,
)


router = APIRouter()


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    tags=["users"]
)
async def create_user(
    request: UserCreateSchema,
    controller: UserController = Depends(ControllerFactory().get_user_controller),
) -> UserResponseSchema:
    """
    Create a user.
    """
    return await controller.create(request=request)


@router.get(
    "/",
    tags=["users"]
)
async def list_users(
    controller: UserController = Depends(ControllerFactory().get_user_controller),
    filters: UserFilter = FilterDepends(UserFilter),
) -> List[UserResponseSchema]:
    """
    List all users.
    """
    return await controller.list(filters=filters)


@router.get(
    "/{id}",
    tags=["users"]
)
async def get_user(
    id: UUID,
    controller: UserController = Depends(ControllerFactory().get_user_controller),
) -> UserResponseSchema:
    """
    Get a user by uuid.
    """
    return await controller.get_by_id(_id=id)


@router.patch(
    "/{id}",
    status_code=status.HTTP_201_CREATED,
    tags=["users"]
)
async def update_user(
    id: UUID,
    request: UserUpdateSchema,
    controller: UserController = Depends(ControllerFactory().get_user_controller),
) -> UserResponseSchema:
    """
    Update a user by uuid.
    """
    return await controller.update_by_id(_id=id, request=request)


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["users"]
)
async def delete_user(
    id: UUID,
    controller: UserController = Depends(ControllerFactory().get_user_controller),
):
    """
    Delete a user by uuid.
    """
    return await controller.delete_by_id(_id=id)
