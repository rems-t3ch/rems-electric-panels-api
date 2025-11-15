from typing import List
from uuid import UUID

from app.domain.model.entities.electronic_panel import ElectronicPanel
from app.interfaces.rest.resources.electronic_panel_resource import (
    ElectronicPanelResource,
    ElectronicPanelCreateResource,
    ElectronicPanelUpdateResource,
    ElectronicPanelListResource,
    ElectronicPanelDeleteResource
)


class ElectronicPanelAssembler:
    """
    Assembler class to convert between domain entities and REST resources.
    """

    @staticmethod
    def to_resource(entity: ElectronicPanel) -> ElectronicPanelResource:
        """
        Convert an ElectronicPanel domain entity to a response resource.
        """
        return ElectronicPanelResource(
            id=entity.id,
            name=entity.name,
            location=entity.location,
            brand=entity.brand,
            amperage_capacity=entity.amperage_capacity,
            state=entity.state,
            year_manufactured=entity.year_manufactured,
            year_installed=entity.year_installed
        )

    @staticmethod
    def to_resource_list(entities: List[ElectronicPanel]) -> ElectronicPanelListResource:
        """
        Convert a list of ElectronicPanel entities to a list response resource.
        """
        panels = [ElectronicPanelAssembler.to_resource(entity) for entity in entities]
        return ElectronicPanelListResource(
            panels=panels,
            total=len(panels)
        )

    @staticmethod
    def to_entity(resource: ElectronicPanelCreateResource, panel_id: UUID = None) -> ElectronicPanel:
        """
        Convert a create resource to a domain entity.
        """
        entity_data = {
            "name": resource.name,
            "location": resource.location,
            "brand": resource.brand,
            "amperage_capacity": resource.amperage_capacity,
            "state": resource.state,
            "year_manufactured": resource.year_manufactured,
            "year_installed": resource.year_installed
        }
        
        if panel_id is not None:
            entity_data["id"] = panel_id
            
        return ElectronicPanel(**entity_data)

    @staticmethod
    def update_entity(entity: ElectronicPanel, resource: ElectronicPanelUpdateResource) -> ElectronicPanel:
        """
        Update an existing ElectronicPanel entity with data from an update resource.
        """
        update_data = resource.model_dump(exclude_unset=True, exclude_none=True)
        
        for field, value in update_data.items():
            setattr(entity, field, value)
        
        return entity

    @staticmethod
    def merge_to_entity(
        resource: ElectronicPanelUpdateResource,
        existing_entity: ElectronicPanel
    ) -> ElectronicPanel:
        """
        Create a new entity by merging update resource data with an existing entity.
        """
        entity_data = {
            "id": existing_entity.id,
            "name": existing_entity.name,
            "location": existing_entity.location,
            "brand": existing_entity.brand,
            "amperage_capacity": existing_entity.amperage_capacity,
            "state": existing_entity.state,
            "year_manufactured": existing_entity.year_manufactured,
            "year_installed": existing_entity.year_installed
        }
        
        update_data = resource.model_dump(exclude_unset=True, exclude_none=True)
        entity_data.update(update_data)
        
        return ElectronicPanel(**entity_data)

    @staticmethod
    def to_delete_response(panel_id: UUID) -> ElectronicPanelDeleteResource:
        """
        Create a delete response resource.
        """
        return ElectronicPanelDeleteResource(
            message=f"Electronic panel with ID {panel_id} successfully deleted."
        )
    
