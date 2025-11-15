from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field

from app.domain.model.value_objects.panel_state import PanelState


class ElectronicPanelCreateResource(BaseModel):
    """
    Request resource for creating a new electronic panel.
    """
    name: str = Field(..., description="Name of the electronic panel")
    location: str = Field(..., description="Physical location of the panel")
    brand: Optional[str] = Field(default=None, description="Brand of the electronic panel")
    amperage_capacity: float = Field(..., description="Amperage capacity in amps")
    state: PanelState = Field(default=PanelState.OPERATIVE, description="Current operational state")
    year_manufactured: int = Field(..., description="Year the panel was manufactured")
    year_installed: int = Field(..., description="Year the panel was installed")

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


class ElectronicPanelUpdateResource(BaseModel):
    """
    Request resource for updating an existing electronic panel.
    """
    name: Optional[str] = Field(None, description="Name of the electronic panel")
    location: Optional[str] = Field(None, description="Physical location of the panel")
    brand: Optional[str] = Field(None, description="Brand of the electronic panel")
    amperage_capacity: Optional[float] = Field(None, description="Amperage capacity in amps")
    state: Optional[PanelState] = Field(None, description="Current operational state")
    year_manufactured: Optional[int] = Field(None, description="Year the panel was manufactured")
    year_installed: Optional[int] = Field(None, description="Year the panel was installed")

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


class ElectronicPanelResource(BaseModel):
    """
    Response resource representing an electronic panel.
    """
    id: UUID = Field(..., description="Unique identifier of the panel")
    name: str = Field(..., description="Name of the electronic panel")
    location: str = Field(..., description="Physical location of the panel")
    brand: Optional[str] = Field(None, description="Brand of the electronic panel")
    amperage_capacity: float = Field(..., description="Amperage capacity in amps")
    state: PanelState = Field(..., description="Current operational state")
    year_manufactured: int = Field(..., description="Year the panel was manufactured")
    year_installed: int = Field(..., description="Year the panel was installed")

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


class ElectronicPanelListResource(BaseModel):
    """
    Response resource for a list of electronic panels.
    """
    panels: list[ElectronicPanelResource] = Field(..., description="List of electronic panels")
    total: int = Field(..., description="Total number of panels")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "panels": [
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


class ElectronicPanelDeleteResource(BaseModel):
    """
    Response resource for deletion confirmation of an electronic panel.
    """
    message: str = Field(..., description="Confirmation message")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "message": "Electronic panel successfully deleted."
                }
            ]
        }
    }
