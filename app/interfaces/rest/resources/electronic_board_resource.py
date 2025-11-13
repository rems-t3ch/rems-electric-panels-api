from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field

from app.domain.model.value_objects.board_state import BoardState


class ElectronicBoardCreateResource(BaseModel):
    """
    Request resource for creating a new electronic board.
    """
    name: str = Field(..., description="Name of the electronic board")
    location: str = Field(..., description="Physical location of the board")
    brand: Optional[str] = Field(default=None, description="Brand of the electronic board")
    amperage_capacity: float = Field(..., description="Amperage capacity in amps")
    state: BoardState = Field(default=BoardState.OPERATIVE, description="Current operational state")
    year_manufactured: int = Field(..., description="Year the board was manufactured")
    year_installed: int = Field(..., description="Year the board was installed")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Main Distribution Panel",
                    "location": "Building A - Basement",
                    "brand": "Siemens",
                    "amperage_capacity": 400.0,
                    "state": "operative",
                    "year_manufactured": 2020,
                    "year_installed": 2021
                }
            ]
        }
    }


class ElectronicBoardUpdateResource(BaseModel):
    """
    Request resource for updating an existing electronic board.
    """
    name: Optional[str] = Field(None, description="Name of the electronic board")
    location: Optional[str] = Field(None, description="Physical location of the board")
    brand: Optional[str] = Field(None, description="Brand of the electronic board")
    amperage_capacity: Optional[float] = Field(None, description="Amperage capacity in amps")
    state: Optional[BoardState] = Field(None, description="Current operational state")
    year_manufactured: Optional[int] = Field(None, description="Year the board was manufactured")
    year_installed: Optional[int] = Field(None, description="Year the board was installed")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "state": "maintenance",
                    "location": "Building A - Floor 2"
                }
            ]
        }
    }


class ElectronicBoardResource(BaseModel):
    """
    Response resource representing an electronic board.
    """
    id: UUID = Field(..., description="Unique identifier of the board")
    name: str = Field(..., description="Name of the electronic board")
    location: str = Field(..., description="Physical location of the board")
    brand: Optional[str] = Field(None, description="Brand of the electronic board")
    amperage_capacity: float = Field(..., description="Amperage capacity in amps")
    state: BoardState = Field(..., description="Current operational state")
    year_manufactured: int = Field(..., description="Year the board was manufactured")
    year_installed: int = Field(..., description="Year the board was installed")

    model_config = {
        "from_attributes": True,
        "json_schema_extra": {
            "examples": [
                {
                    "id": "550e8400-e29b-41d4-a716-446655440000",
                    "name": "Main Distribution Panel",
                    "location": "Building A - Basement",
                    "brand": "Siemens",
                    "amperage_capacity": 400.0,
                    "state": "operative",
                    "year_manufactured": 2020,
                    "year_installed": 2021
                }
            ]
        }
    }


class ElectronicBoardListResource(BaseModel):
    """
    Response resource for a list of electronic boards.
    """
    boards: list[ElectronicBoardResource] = Field(..., description="List of electronic boards")
    total: int = Field(..., description="Total number of boards")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "boards": [
                        {
                            "id": "550e8400-e29b-41d4-a716-446655440000",
                            "name": "Main Distribution Panel",
                            "location": "Building A - Basement",
                            "brand": "Siemens",
                            "amperage_capacity": 400.0,
                            "state": "operative",
                            "year_manufactured": 2020,
                            "year_installed": 2021
                        }
                    ],
                    "total": 1
                }
            ]
        }
    }
