from uuid import UUID
from typing import List, Optional

from app.domain.model.entities.electronic_board import ElectronicBoard
from app.domain.repositories.electronic_board_repository import ElectronicBoardRepository
from app.domain.services.electronic_board_service import ElectronicBoardService

class ElectronicBoardServiceImpl(ElectronicBoardService):
    """
    Electronic Board Service Implementation
    
    It applies business rules and manages the flow of operations.
    """
    
    def __init__(self, repository: ElectronicBoardRepository):
        """
        Initialize the service with a repository.
        
        Args:
            repository: The repository for data access operations.
        """
        self._electronic_board_repository = repository
    
    async def create_board(self, board: ElectronicBoard) -> ElectronicBoard:
        """
        Create a new electronic board.
        
        Args:
            board: The board entity to create.
            
        Returns:
            The created board with its generated ID.
            
        Raises:
            ValueError: If validation fails at the domain level.
        """
        
        created_board = await self._electronic_board_repository.create(board)
        
        return created_board
    
    async def get_board_by_id(self, board_id: UUID) -> Optional[ElectronicBoard]:
        """
        Retrieve an electronic board by its ID.
        
        Args:
            board_id: The unique identifier of the board.
            
        Returns:
            The board if found, None otherwise.
        """
        return await self._electronic_board_repository.get_by_id(board_id)
    
    async def list_all_boards(self) -> List[ElectronicBoard]:
        """
        List all electronic boards.
        
        Returns:
            List of all boards in the system.
        """
        
        return await self._electronic_board_repository.list_all()
    
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
        existing_entity = await self._electronic_board_repository.get_by_id(board_id)
        
        if existing_entity is None:
            raise ValueError(f"Electronic board with ID {board_id} not found")
        
        
        updated_board = await self._electronic_board_repository.update(board)
        
        return updated_board
    
    async def delete_board(self, board_id: UUID) -> None:
        """
        Delete an electronic board by its ID.
        
        Args:
            board_id: The unique identifier of the board to delete.
            
        Raises:
            ValueError: If board not found.
        """
        exists = await self._electronic_board_repository.exists(board_id)
        
        if not exists:
            raise ValueError(f"Electronic board with ID {board_id} not found")
        
        await self._electronic_board_repository.delete(board_id)