from uuid import UUID
from typing import TYPE_CHECKING, List, Optional

from sqlmodel import select
from sqlalchemy.ext.asyncio.session import AsyncSession, async_sessionmaker
from app.domain.repositories.electronic_board_repository import ElectronicBoardRepository

from app.domain.model.entities.electronic_board import ElectronicBoard
    
class ElectronicBoardSQLModelRepository(ElectronicBoardRepository):
    """
    SQLModel-based implementation of the ElectronicBoardRepository.

    This repository uses and AsyncSession to interact with a SQLite database in an asynchronous way.
    """
    def __init__(self, session_factory: async_sessionmaker[AsyncSession]) -> None:
        self._session_factory = session_factory

    async def create(self, board: ElectronicBoard) -> ElectronicBoard:
        """
        Create a new ElectronicBoard entity.
        """
        async with self._session_factory() as session:
            async with session.begin():
                session.add(board)
            await session.refresh(board)
            return board
    
    async def get_by_id(self, board_id: UUID) -> Optional[ElectronicBoard]:
        """
        Retrieve an ElectronicBoard entity by its unique identifier.
        """
        async with self._session_factory() as session:
            board = await session.get(ElectronicBoard, board_id)
            return board
    
    async def list_all(self) -> List[ElectronicBoard]:
        """
        List all ElectronicBoard entities.
        """
        statement = select(ElectronicBoard)
        async with self._session_factory() as session:
            results = await session.execute(statement)
            boards = results.scalars().all()
            return boards
    
    async def update(self, board: ElectronicBoard) -> ElectronicBoard:
        """
        Update an existing ElectronicBoard entity.
        """
        async with self._session_factory() as session:
            async with session.begin():
                session.add(board)
            await session.refresh(board)
            return board
    

    async def delete(self, board_id: UUID) -> bool:
        """
        Delete an ElectronicBoard entity by its unique identifier.
        """
        async with self._session_factory() as session:
            async with session.begin():
                board = await session.get(ElectronicBoard, board_id)
                if board is not None:
                    session.delete(board)
            return True