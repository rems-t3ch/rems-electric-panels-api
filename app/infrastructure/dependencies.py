from app.infrastructure.db import get_async_session_factory
from app.domain.services.electronic_panel_service import ElectronicPanelService
from app.application.internal.services.electronic_panel_service_impl import ElectronicPanelServiceImpl
from app.infrastructure.repositories.electronic_panel_sqlmodel_repository import ElectronicPanelSQLModelRepository

def get_electronic_panel_service() -> ElectronicPanelService:
    """
    Factory function for Electronic Panel Service.
    
    Creates the complete dependency chain:
    Session Factory → Repository → Service
    
    Returns:
        ElectronicPanelService: A configured service instance.
    """
    session_factory = get_async_session_factory()
    repository = ElectronicPanelSQLModelRepository(session_factory)
    return ElectronicPanelServiceImpl(repository)
