"""
Base data repository with basic implementations of CRUD operations on the database.
"""

from fastapi_filter.contrib.sqlalchemy import Filter
from sqlalchemy.sql.expression import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from typing import Type, TypeVar, Generic, List
from uuid import UUID

from messenger.models import Base
from messenger.database import get_session
from messenger.exceptions import IntegrityErrorException, NotFoundException


ModelType = TypeVar("ModelType", bound=Base)


class BaseRepo(Generic[ModelType]):
    """
    Base data repository.
    """
    def __init__(
        self,
        db_session: AsyncSession,
        model: Type[ModelType],
    ):
        self.session = db_session
        self.model = model


    async def list(
        self,
        filters: Filter,
    ) -> List[ModelType]:
        """
        Lists all model objects from the database.
        """
        query = filters.filter(select(self.model))
        db_obj = await self.session.scalars(query)
        res = db_obj.all()
        return res


    async def create(
        self,
        model_obj: Type[ModelType],
    ) -> ModelType:
        """
        Creates and returns a model object from the database.
        """
        self.session.add(model_obj)
        try:
            await self.session.commit()
            await self.session.refresh(model_obj)
        except IntegrityError as e:
            raise IntegrityErrorException(message=str(e.orig))
        return model_obj


    async def get_by_id(
        self,
        _id: UUID,
    ) -> ModelType:
        """
        Returns a model object from the database by uuid.
        """
        query = select(self.model).where(self.model.id == _id)
        db_obj = await self.session.scalars(query)
        res = db_obj.one_or_none()
        if not res:
            raise NotFoundException(message=f"{_id} not found.")
        return res


    async def update(
        self,
        model_obj: Type[ModelType],
    ) -> ModelType:
        """
        Updates and retunrs a model object from the database by uuid.
        """
        try:
            self.session.add(model_obj)
            await self.session.commit()
            await self.session.refresh(model_obj)
        except IntegrityError:
            raise IntegrityErrorException
        return model_obj


    async def delete(
        self,
        model_obj: Type[ModelType],
    ):
        """
        Deletes a model object from the database by uuid.
        """
        try:
            await self.session.delete(model_obj)
            self.session.commit()
        except IntegrityError:
            raise IntegrityErrorException
