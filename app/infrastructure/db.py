from typing import AsyncIterator

from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.domain.model.entities.electronic_board import ElectronicBoard

DATABASE_URL = "sqlite+aiosqlite:///./boards.db"

async_engine = create_async_engine(
    DATABASE_URL,
    echo=True,
)

async_session_factory = async_sessionmaker(
    bind=async_engine,
    expire_on_commit=False,
)

async def init_db() -> None:
    """
    Create database tables (async).
    """
    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

async def get_session() -> AsyncIterator[AsyncSession]:
    """
    Dependency to get an async database session.
    """
    async with async_session_factory() as session:
        yield session

def get_async_session_factory() -> async_sessionmaker[AsyncSession]:
    """
    Get the async session factory for database interactions.
    """
    return async_session_factory