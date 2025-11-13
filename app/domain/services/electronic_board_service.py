from abc import ABC, abstractmethod
from uuid import UUID
from typing import List, Optional

from app.domain.model.entities.electronic_board import ElectronicBoard


class ElectronicBoardService(ABC):
    """
    Abstract service interface for Electronic Board business operations.

    Methods:
        - create_board(board: ElectronicBoard) -> ElectronicBoard
        - get_board_by_id(board_id: UUID) -> Optional[ElectronicBoard]
        - list_all_boards() -> List[ElectronicBoard]
        - update_board(board: ElectronicBoard) -> ElectronicBoard
        - delete_board(board_id: UUID) -> bool
        - board_exists(board_id: UUID) -> bool
    """
    
    @abstractmethod
    async def create_board(self, board: ElectronicBoard) -> ElectronicBoard:
        """
        Create a new electronic board.
        
        Args:
            board: The board entity to create.
            
        Returns:
            The created board.

        Raises:
            ValueError: If validation fails at the domain level.
        """
        raise NotImplementedError()
    
    @abstractmethod
    async def get_board_by_id(self, board_id: UUID) -> Optional[ElectronicBoard]:
        """
        Retrieve an electronic board by its ID.
        
        Args:
            board_id: The unique identifier of the board.
            
        Returns:
            The board if found, None otherwise.
        """
        raise NotImplementedError()
    
    @abstractmethod
    async def list_all_boards(self) -> List[ElectronicBoard]:
        """
        List all electronic boards.
        
        Returns:
            List of all boards in the system.
        """
        raise NotImplementedError()
    
    @abstractmethod
    async def update_board(self, board_id: UUID, board: ElectronicBoard) -> ElectronicBoard:
        """
        Update an existing electronic board.
        
        Args:
            board_id: The unique identifier of the board to update.
            board: The board entity with updated values.
            
        Returns:
            The updated board.
            
        Raises:
            ValueError: If board not found or validation fails.
        """
        raise NotImplementedError()
    
    @abstractmethod
    async def delete_board(self, board_id: UUID) -> None:
        """
        Delete an electronic board by its ID.
        
        Args:
            board_id: The unique identifier of the board to delete.
            
        Raises:
            ValueError: If board not found.
        """
        raise NotImplementedError()
    