from abc import ABC, abstractmethod
from uuid import UUID
from typing import List, Optional

from app.domain.model.entities.electronic_panel import ElectronicPanel


class ElectronicPanelService(ABC):
    """
    Abstract service interface for Electronic Panel business operations.
    """
    
    @abstractmethod
    async def create_panel(self, panel: ElectronicPanel) -> ElectronicPanel:
        raise NotImplementedError()
    
    @abstractmethod
    async def get_panel_by_id(self, panel_id: UUID) -> Optional[ElectronicPanel]:
        raise NotImplementedError()
    
    @abstractmethod
    async def list_all_panels(self) -> List[ElectronicPanel]:
        raise NotImplementedError()
    
    @abstractmethod
    async def update_panel(self, panel_id: UUID, panel: ElectronicPanel) -> ElectronicPanel:
        raise NotImplementedError()
    
    @abstractmethod
    async def delete_panel(self, panel_id: UUID) -> None:
        raise NotImplementedError()
