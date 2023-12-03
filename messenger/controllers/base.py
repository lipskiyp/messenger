"""
Base data controller.
"""

from fastapi_filter.contrib.sqlalchemy import Filter
from sqlalchemy.sql import func
from typing import Type, TypeVar, Generic, List, Any
from uuid import UUID

from messenger.models import Base
from messenger.repositories import BaseRepo


ModelType = TypeVar("ModelType", bound=Base)


class BaseController(Generic[ModelType]):
    """
    Base controller for CRUD operations on the database.
    """
    def __init__(
        self,
        repository: BaseRepo,
        model: Type[ModelType]
    ):
        self.model = model
        self.repository = repository


    async def list(
        self,
        filters: Filter,
    ) -> List[ModelType]:
        """
        Lists all model objects from the database.
        """
        return await self.repository.list(filters=filters)


    async def create(
        self,
        request: dict[str, Any],
    ) -> ModelType:
        """
        Creates and returns a model object from the database.
        """
        model_obj = self.model(**request.model_dump())
        return await self.repository.create(model_obj)


    async def get_by_id(
        self,
        _id: UUID,
    ) -> ModelType:
        """
        Returns a model object from the database by uuid.
        """
        return await self.repository.get_by_id(_id=_id)


    async def update_by_id(
        self,
        _id: UUID,
        request: dict[str, Any],
    ) -> ModelType:
        """
        Updates and retunrs a model object from the database by uuid.
        """
        model_obj = await self.get_by_id(_id=_id)
        for key, value in request.model_dump(exclude_unset=True).items():
            setattr(model_obj, key, value)
        return await self.repository.update(model_obj=model_obj)


    async def delete_by_id(
        self,
        _id: UUID,
    ):
        """
        Deletes a model object from the database by uuid.
        """
        model_obj = await self.get_by_id(_id=_id)
        return await self.repository.delete(model_obj=model_obj)
