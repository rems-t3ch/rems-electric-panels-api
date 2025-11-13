from typing import List
from uuid import UUID

from app.domain.model.entities.electronic_board import ElectronicBoard
from app.interfaces.rest.resources.electronic_board_resource import (
    ElectronicBoardResource,
    ElectronicBoardCreateResource,
    ElectronicBoardUpdateResource,
    ElectronicBoardListResource,
    ElectronicBoardDeleteResource
)


class ElectronicBoardAssembler:
    """
    Assembler class to convert between domain entities and REST resources.
    """

    @staticmethod
    def to_resource(entity: ElectronicBoard) -> ElectronicBoardResource:
        """
        Convert an ElectronicBoard domain entity to a response resource.
        
        Args:
            entity: The domain entity to convert.
            
        Returns:
            ElectronicBoardResource: The REST API resource representation.
        """
        return ElectronicBoardResource(
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
    def to_resource_list(entities: List[ElectronicBoard]) -> ElectronicBoardListResource:
        """
        Convert a list of ElectronicBoard entities to a list response resource.
        
        Args:
            entities: List of domain entities to convert.
            
        Returns:
            ElectronicBoardListResource: The REST API list resource with metadata.
        """
        boards = [ElectronicBoardAssembler.to_resource(entity) for entity in entities]
        return ElectronicBoardListResource(
            boards=boards,
            total=len(boards)
        )

    @staticmethod
    def to_entity(resource: ElectronicBoardCreateResource, board_id: UUID = None) -> ElectronicBoard:
        """
        Convert a create resource to a domain entity.
        
        Args:
            resource: The create resource from the API request.
            board_id: Optional UUID to assign to the entity (for testing or specific cases).
            
        Returns:
            ElectronicBoard: The domain entity.
            
        Note:
            The entity's validators will run during instantiation, ensuring data integrity.
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
        
        if board_id is not None:
            entity_data["id"] = board_id
            
        return ElectronicBoard(**entity_data)

    @staticmethod
    def update_entity(entity: ElectronicBoard, resource: ElectronicBoardUpdateResource) -> ElectronicBoard:
        """
        Update an existing ElectronicBoard entity with data from an update resource.
        
        Args:
            entity: The existing domain entity to update.
            resource: The update resource containing the new values.
            
        Returns:
            ElectronicBoard: The updated domain entity.
            
        Note:
            Only fields present (not None) in the resource are updated.
            The entity's validators will run when setting new values.
        """
        update_data = resource.model_dump(exclude_unset=True, exclude_none=True)
        
        for field, value in update_data.items():
            setattr(entity, field, value)
        
        return entity

    @staticmethod
    def merge_to_entity(
        resource: ElectronicBoardUpdateResource,
        existing_entity: ElectronicBoard
    ) -> ElectronicBoard:
        """
        Create a new entity by merging update resource data with an existing entity.
        
        Args:
            resource: The update resource with new values.
            existing_entity: The current entity state.
            
        Returns:
            ElectronicBoard: A new entity instance with merged data.
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
        
        return ElectronicBoard(**entity_data)

    @staticmethod
    def to_delete_response(board_id: UUID) -> ElectronicBoardDeleteResource:
        """
        Create a delete response resource.
        
        Args:
            board_id: The UUID of the deleted board.
            
        Returns:
            ElectronicBoardDeleteResource: Confirmation message for the deletion.
        """
        return ElectronicBoardDeleteResource(
            message=f"Electronic board with ID {board_id} successfully deleted."
        )
    
    