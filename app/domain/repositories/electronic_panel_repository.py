from uuid import UUID
from typing import TYPE_CHECKING, List, Optional
from abc import ABC, abstractmethod
from app.domain.model.entities.electronic_panel import ElectronicPanel

class ElectronicPanelRepository(ABC):
    """
    Abstract repository interface for managing ElectronicPanel entities.
    """
    @abstractmethod
    async def create(self, panel: ElectronicPanel) -> ElectronicPanel:
        raise NotImplementedError()
    
    @abstractmethod
    async def get_by_id(self, panel_id: UUID) -> Optional[ElectronicPanel]:
        raise NotImplementedError()
    
    @abstractmethod
    async def list_all(self) -> List[ElectronicPanel]:
        raise NotImplementedError()
    
    @abstractmethod
    async def update(self, panel: ElectronicPanel) -> ElectronicPanel:
        raise NotImplementedError()
    
    @abstractmethod
    async def delete(self, panel_id: UUID) -> bool:
        raise NotImplementedError()

    @abstractmethod
    async def exists(self, panel_id: UUID) -> bool:
        raise NotImplementedError()
