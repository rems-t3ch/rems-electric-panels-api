from uuid import UUID
from typing import TYPE_CHECKING, List, Optional

from sqlmodel import select
from sqlalchemy.ext.asyncio.session import AsyncSession, async_sessionmaker
from app.domain.repositories.electronic_panel_repository import ElectronicPanelRepository

from app.domain.model.entities.electronic_panel import ElectronicPanel
    
class ElectronicPanelSQLModelRepository(ElectronicPanelRepository):
    """
    SQLModel-based implementation of the ElectronicPanelRepository.

    This repository uses an AsyncSession to interact with a database asynchronously.
    """
    def __init__(self, session_factory: async_sessionmaker[AsyncSession]) -> None:
        self._session_factory = session_factory

    async def create(self, panel: ElectronicPanel) -> ElectronicPanel:
        async with self._session_factory() as session:
            async with session.begin():
                session.add(panel)
            await session.refresh(panel)
            return panel
    
    async def get_by_id(self, panel_id: UUID) -> Optional[ElectronicPanel]:
        async with self._session_factory() as session:
            panel = await session.get(ElectronicPanel, panel_id)
            return panel
    
    async def list_all(self) -> List[ElectronicPanel]:
        statement = select(ElectronicPanel)
        async with self._session_factory() as session:
            results = await session.execute(statement)
            panels = results.scalars().all()
            return panels
    
    async def update(self, panel: ElectronicPanel) -> ElectronicPanel:
        async with self._session_factory() as session:
            async with session.begin():
                session.add(panel)
            await session.refresh(panel)
            return panel
    

    async def delete(self, panel_id: UUID) -> bool:
        async with self._session_factory() as session:
            async with session.begin():
                panel = await session.get(ElectronicPanel, panel_id)
                if panel is not None:
                    await session.delete(panel)
                    return True
            return False

    async def exists(self, panel_id: UUID) -> bool:
        statement = select(ElectronicPanel.id).where(ElectronicPanel.id == panel_id)
        async with self._session_factory() as session:
            results = await session.execute(statement)
            return results.scalar_one_or_none() is not None
