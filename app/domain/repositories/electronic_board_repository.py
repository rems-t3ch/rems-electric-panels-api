from uuid import UUID
from typing import TYPE_CHECKING, List, Optional
from abc import ABC, abstractmethod

if TYPE_CHECKING:
    from app.domain.model.entities.electronic_board import ElectronicBoard

class ElectronicBoardRepository(ABC):
    """
    Abstract repository interface for managing ElectronicBoard entities.
    
    Methods:
        - create(board: ElectronicBoard) -> ElectronicBoard
        - get_by_id(board_id: UUID) -> Optional[ElectronicBoard]
        - list_all() -> List[ElectronicBoard]
        - update(board: ElectronicBoard) -> ElectronicBoard
        - delete(board_id: UUID) -> None
    """
    @abstractmethod
    async def create(self, board: ElectronicBoard) -> ElectronicBoard:
        """
        Create a new ElectronicBoard entity.
        """
        raise NotImplementedError()
    
    @abstractmethod
    async def get_by_id(self, board_id: UUID) -> Optional[ElectronicBoard]:
        """
        Retrieve an ElectronicBoard entity by its unique identifier.
        """
        raise NotImplementedError()
    
    @abstractmethod
    async def list_all(self) -> List[ElectronicBoard]:
        """
        List all ElectronicBoard entities.
        """
        raise NotImplementedError()
    
    @abstractmethod
    async def update(self, board: ElectronicBoard) -> ElectronicBoard:
        """
        Update an existing ElectronicBoard entity.
        """
        raise NotImplementedError()
    
    @abstractmethod
    async def delete(self, board_id: UUID) -> None:
        """
        Delete an ElectronicBoard entity by its unique identifier.
        """
        raise NotImplementedError()
