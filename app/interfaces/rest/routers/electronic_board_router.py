from uuid import UUID
from fastapi import APIRouter, HTTPException, status, Depends

from app.interfaces.rest.resources.electronic_board_resource import (
    ElectronicBoardResource,
    ElectronicBoardCreateResource,
    ElectronicBoardUpdateResource,
    ElectronicBoardListResource,
    ElectronicBoardDeleteResource
)

from app.interfaces.rest.transforms.electronic_board_assembler import ElectronicBoardAssembler
from app.domain.services.electronic_board_service import ElectronicBoardService
from app.infrastructure.dependencies import get_electronic_board_service

router = APIRouter(prefix="/boards", tags=["Electronic Boards"])

@router.post(
    "",
    response_model=ElectronicBoardResource,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new electronic board",
    description="Create a new electronic board with the provided information. Validation is performed at the domain level."
)
async def create_board(
    resource: ElectronicBoardCreateResource,
    service: ElectronicBoardService = Depends(get_electronic_board_service)
) -> ElectronicBoardResource:
    """
    Create a new electronic board.
    
    Args:
        resource: The board data from the request body.
        service: The injected service instance.
        
    Returns:
        The created board resource with generated ID.
        
    Raises:
        HTTPException: 400 if validation fails at domain level.
    """
    try:
        entity = ElectronicBoardAssembler.to_entity(resource)
        
        created_entity = await service.create_board(entity)
        
        return ElectronicBoardAssembler.to_resource(created_entity)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.get(
    "",
    response_model=ElectronicBoardListResource,
    summary="List all electronic boards",
    description="Retrieve a list of all electronic boards in the system."
)
async def list_boards(
    service: ElectronicBoardService = Depends(get_electronic_board_service)
) -> ElectronicBoardListResource:
    """
    List all electronic boards.
    
    Args:
        service: The injected service instance.
        
    Returns:
        A list resource containing all boards and metadata.
    """
    entities = await service.list_all_boards()
    return ElectronicBoardAssembler.to_resource_list(entities)


@router.get(
    "/{board_id}",
    response_model=ElectronicBoardResource,
    summary="Get an electronic board by ID",
    description="Retrieve a specific electronic board by its unique identifier."
)
async def get_board(
    board_id: UUID,
    service: ElectronicBoardService = Depends(get_electronic_board_service)
) -> ElectronicBoardResource:
    """
    Get a board by ID.
    
    Args:
        board_id: The unique identifier of the board.
        service: The injected service instance.
        
    Returns:
        The board resource.
        
    Raises:
        HTTPException: 404 if board not found.
    """
    entity = await service.get_board_by_id(board_id)
    
    if entity is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Electronic board with ID {board_id} not found"
        )
    
    return ElectronicBoardAssembler.to_resource(entity)


@router.put(
    "/{board_id}",
    response_model=ElectronicBoardResource,
    summary="Update an electronic board",
    description="Update an existing electronic board. Only provided fields are updated (partial update supported)."
)
async def update_board(
    board_id: UUID,
    resource: ElectronicBoardUpdateResource,
    service: ElectronicBoardService = Depends(get_electronic_board_service)
) -> ElectronicBoardResource:
    """
    Update a board.
    
    Args:
        board_id: The unique identifier of the board.
        resource: The update data from the request body.
        service: The injected service instance.
        
    Returns:
        The updated board resource.
        
    Raises:
        HTTPException: 404 if board not found, 400 if validation fails.
    """
    try:
        existing_entity = await service.get_board_by_id(board_id)
        
        if existing_entity is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Electronic board with ID {board_id} not found"
            )
        
        updated_entity = ElectronicBoardAssembler.update_entity(existing_entity, resource)
        
        updated_entity = await service.update_board(board_id, updated_entity)
        
        return ElectronicBoardAssembler.to_resource(updated_entity)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.delete(
    "/{board_id}",
    response_model=ElectronicBoardDeleteResource,
    status_code=status.HTTP_200_OK,
    summary="Delete an electronic board",
    description="Delete an electronic board by its unique identifier."
)
async def delete_board(
    board_id: UUID,
    service: ElectronicBoardService = Depends(get_electronic_board_service)
) -> ElectronicBoardDeleteResource:
    """
    Delete a board.
    
    Args:
        board_id: The unique identifier of the board.
        service: The injected service instance.
        
    Returns:
        Confirmation message for the deletion.
        
    Raises:
        HTTPException: 404 if board not found.
    """
    try:
        await service.delete_board(board_id)
        return ElectronicBoardAssembler.to_delete_response(board_id)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )

