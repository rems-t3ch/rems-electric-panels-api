from uuid import UUID
from fastapi import APIRouter, HTTPException, status, Depends

from app.interfaces.rest.resources.electronic_board_resource import (
    ElectronicBoardResource,
    ElectronicBoardCreateResource,
    ElectronicBoardUpdateResource,
    ElectronicBoardListResource
)

from app.infrastructure.db import get_async_session_factory
from app.infrastructure.repositories.electronic_board_sqlmodel_repository import ElectronicBoardSQLModelRepository

from app.domain.repositories.electronic_board_repository import ElectronicBoardRepository
from app.interfaces.rest.transforms.electronic_board_assembler import ElectronicBoardAssembler

router = APIRouter(prefix="/boards", tags=["Electronic Boards"])

async def get_repository() -> ElectronicBoardRepository:
    """
    Dependency to get the repository instance.
    """
    session_factory = get_async_session_factory()
    return ElectronicBoardSQLModelRepository(session_factory)


@router.post(
    "",
    response_model=ElectronicBoardResource,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new electronic board",
    description="Create a new electronic board with the provided information. Validation is performed at the domain level."
)
async def create_board(
    resource: ElectronicBoardCreateResource,
    repository: ElectronicBoardRepository = Depends(get_repository)
) -> ElectronicBoardResource:
    """
    Create a new electronic board.
    
    Args:
        resource: The board data from the request body.
        repository: The injected repository instance.
        
    Returns:
        The created board resource with generated ID.
        
    Raises:
        HTTPException: 400 if validation fails at domain level.
    """
    try:
        entity = ElectronicBoardAssembler.to_entity(resource)
        
        created_entity = await repository.create(entity)
        
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
    repository: ElectronicBoardRepository = Depends(get_repository)
) -> ElectronicBoardListResource:
    """
    List all electronic boards.
    
    Args:
        repository: The injected repository instance.
        
    Returns:
        A list resource containing all boards and metadata.
    """
    entities = await repository.list_all()
    return ElectronicBoardAssembler.to_resource_list(entities)


@router.get(
    "/{board_id}",
    response_model=ElectronicBoardResource,
    summary="Get an electronic board by ID",
    description="Retrieve a specific electronic board by its unique identifier."
)
async def get_board(
    board_id: UUID,
    repository: ElectronicBoardRepository = Depends(get_repository)
) -> ElectronicBoardResource:
    """
    Get a board by ID.
    
    Args:
        board_id: The unique identifier of the board.
        repository: The injected repository instance.
        
    Returns:
        The board resource.
        
    Raises:
        HTTPException: 404 if board not found.
    """
    entity = await repository.get_by_id(board_id)
    
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
    repository: ElectronicBoardRepository = Depends(get_repository)
) -> ElectronicBoardResource:
    """
    Update a board.
    
    Args:
        board_id: The unique identifier of the board.
        resource: The update data from the request body.
        repository: The injected repository instance.
        
    Returns:
        The updated board resource.
        
    Raises:
        HTTPException: 404 if board not found, 400 if validation fails.
    """
   
    existing_entity = await repository.get_by_id(board_id)
    
    if existing_entity is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Electronic board with ID {board_id} not found"
        )
    
    try:

        updated_entity = ElectronicBoardAssembler.update_entity(existing_entity, resource)
        
        updated_entity = await repository.update(updated_entity)
        
        return ElectronicBoardAssembler.to_resource(updated_entity)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.delete(
    "/{board_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete an electronic board",
    description="Delete an electronic board by its unique identifier."
)
async def delete_board(
    board_id: UUID,
    repository: ElectronicBoardRepository = Depends(get_repository)
) -> None:
    """
    Delete a board.
    
    Args:
        board_id: The unique identifier of the board.
        repository: The injected repository instance.
        
    Raises:
        HTTPException: 404 if board not found.
    """
    existing_entity = await repository.get_by_id(board_id)
    
    if existing_entity is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Electronic board with ID {board_id} not found"
        )
    
    await repository.delete(board_id)
