from uuid import UUID
from fastapi import APIRouter, HTTPException, status, Depends

from app.interfaces.rest.resources.electronic_panel_resource import (
    ElectronicPanelResource,
    ElectronicPanelCreateResource,
    ElectronicPanelUpdateResource,
    ElectronicPanelListResource,
    ElectronicPanelDeleteResource
)

from app.interfaces.rest.transforms.electronic_panel_assembler import ElectronicPanelAssembler
from app.domain.services.electronic_panel_service import ElectronicPanelService
from app.infrastructure.dependencies import get_electronic_panel_service

router = APIRouter(prefix="/panels", tags=["Electronic Panels"])

@router.post(
    "",
    response_model=ElectronicPanelResource,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new electronic panel",
    description="Create a new electronic panel with the provided information. Validation is performed at the domain level."
)
async def create_panel(
    resource: ElectronicPanelCreateResource,
    service: ElectronicPanelService = Depends(get_electronic_panel_service)
) -> ElectronicPanelResource:
    try:
        entity = ElectronicPanelAssembler.to_entity(resource)
        created_entity = await service.create_panel(entity)
        return ElectronicPanelAssembler.to_resource(created_entity)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.get(
    "",
    response_model=ElectronicPanelListResource,
    summary="List all electronic panels",
    description="Retrieve a list of all electronic panels in the system."
)
async def list_panels(
    service: ElectronicPanelService = Depends(get_electronic_panel_service)
) -> ElectronicPanelListResource:
    entities = await service.list_all_panels()
    return ElectronicPanelAssembler.to_resource_list(entities)


@router.get(
    "/{panel_id}",
    response_model=ElectronicPanelResource,
    summary="Get an electronic panel by ID",
    description="Retrieve a specific electronic panel by its unique identifier."
)
async def get_panel(
    panel_id: UUID,
    service: ElectronicPanelService = Depends(get_electronic_panel_service)
) -> ElectronicPanelResource:
    entity = await service.get_panel_by_id(panel_id)
    if entity is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Electronic panel with ID {panel_id} not found"
        )
    return ElectronicPanelAssembler.to_resource(entity)


@router.put(
    "/{panel_id}",
    response_model=ElectronicPanelResource,
    summary="Update an electronic panel",
    description="Update an existing electronic panel. Only provided fields are updated (partial update supported)."
)
async def update_panel(
    panel_id: UUID,
    resource: ElectronicPanelUpdateResource,
    service: ElectronicPanelService = Depends(get_electronic_panel_service)
) -> ElectronicPanelResource:
    try:
        existing_entity = await service.get_panel_by_id(panel_id)
        if existing_entity is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Electronic panel with ID {panel_id} not found"
            )
        updated_entity = ElectronicPanelAssembler.update_entity(existing_entity, resource)
        updated_entity = await service.update_panel(panel_id, updated_entity)
        return ElectronicPanelAssembler.to_resource(updated_entity)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.delete(
    "/{panel_id}",
    response_model=ElectronicPanelDeleteResource,
    status_code=status.HTTP_200_OK,
    summary="Delete an electronic panel",
    description="Delete an electronic panel by its unique identifier."
)
async def delete_panel(
    panel_id: UUID,
    service: ElectronicPanelService = Depends(get_electronic_panel_service)
) -> ElectronicPanelDeleteResource:
    try:
        await service.delete_panel(panel_id)
        return ElectronicPanelAssembler.to_delete_response(panel_id)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
