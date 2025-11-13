from app.infrastructure.db import get_async_session_factory
from app.domain.services.electronic_board_service import ElectronicBoardService
from app.application.internal.services.electronic_board_service_impl import ElectronicBoardServiceImpl
from app.infrastructure.repositories.electronic_board_sqlmodel_repository import ElectronicBoardSQLModelRepository

def get_electronic_board_service() -> ElectronicBoardService:
    """
    Factory function for Electronic Board Service.
    
    Creates the complete dependency chain:
    Session Factory → Repository → Service
    
    Returns:
        ElectronicBoardService: A configured service instance.
    """
    session_factory = get_async_session_factory()
    repository = ElectronicBoardSQLModelRepository(session_factory)
    return ElectronicBoardServiceImpl(repository)
