from uuid import UUID
from typing import List, Optional

from app.domain.model.entities.electronic_panel import ElectronicPanel
from app.domain.repositories.electronic_panel_repository import ElectronicPanelRepository
from app.domain.services.electronic_panel_service import ElectronicPanelService

class ElectronicPanelServiceImpl(ElectronicPanelService):
    """
    Electronic Panel Service Implementation
    """
    
    def __init__(self, repository: ElectronicPanelRepository):
        self._electronic_panel_repository = repository
    
    async def create_panel(self, panel: ElectronicPanel) -> ElectronicPanel:
        created_panel = await self._electronic_panel_repository.create(panel)
        return created_panel
    
    async def get_panel_by_id(self, panel_id: UUID) -> Optional[ElectronicPanel]:
        return await self._electronic_panel_repository.get_by_id(panel_id)
    
    async def list_all_panels(self) -> List[ElectronicPanel]:
        return await self._electronic_panel_repository.list_all()
    
    async def update_panel(self, panel_id: UUID, panel: ElectronicPanel) -> ElectronicPanel:
        existing_entity = await self._electronic_panel_repository.get_by_id(panel_id)
        if existing_entity is None:
            raise ValueError(f"Electronic panel with ID {panel_id} not found")
        updated_panel = await self._electronic_panel_repository.update(panel)
        return updated_panel
    
    async def delete_panel(self, panel_id: UUID) -> None:
        exists = await self._electronic_panel_repository.exists(panel_id)
        if not exists:
            raise ValueError(f"Electronic panel with ID {panel_id} not found")
        await self._electronic_panel_repository.delete(panel_id)
