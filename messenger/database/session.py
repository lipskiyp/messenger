"""
Database connection.
"""

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from messenger.settings import settings
from messenger.models import Base


engine = create_async_engine(
    settings.get_db_url(),
    #echo=True,
)


async def init_db():
    """
    Initiate database (NB will drop current tables).
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def get_session() -> AsyncSession:
    """
    Get async database session (for endpoint dependency injection).
    """
    session = async_sessionmaker(
        bind=engine
    )
    async with session() as db_session:
        try:
            yield db_session
        finally:
            await db_session.close()
