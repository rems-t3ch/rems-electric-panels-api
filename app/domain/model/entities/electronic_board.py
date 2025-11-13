import uuid 
from datetime import date
from typing import Optional
from sqlmodel import SQLModel, Field 

from pydantic import (
    ValidationInfo,
    field_validator as validator
)

from app.domain.model.value_objects.board_state import BoardState

class ElectronicBoard(SQLModel, table=True):
    """
    Represents an electronic board in the system.

    Attributes:
        id (uuid.UUID): Unique identifier for the electronic board.
        name (str): Name of the electronic board.
        location (str): Physical location of the electronic board.
        brand (Optional[str]): Brand of the electronic board.
        amperage_capacity (float): Amperage capacity of the electronic board.
        state (BoardState): Current state of the electronic board.
        year_manufactured (int): Year the electronic board was manufactured.
        year_installed (int): Year the electronic board was installed.
    """
    
    __tablename__ = "electronic_boards"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
    
    name: str = Field(..., min_length=1, max_length=200)
    location: str = Field(..., min_length=1, max_length=200)
    brand: Optional[str] = Field(default=None, max_length=100)
    
    amperage_capacity: float = Field(..., gt=0)
    state: BoardState = Field(default=BoardState.OPERATIVE)
    year_manufactured: int = Field(..., ge=1900)
    year_installed: int = Field(..., ge=1900)

    @validator("year_installed", mode="after")
    def _installed_after_manufactured(cls, value: int, info: ValidationInfo):
        """
        Ensure that year_installed is not earlier than year_manufactured.
        """
        year_manu = info.data.get("year_manufactured")
        
        if year_manu is not None and value < year_manu:
            raise ValueError("year_installed must be >= year_manufactured")
        
        return value

    @validator("year_manufactured", "year_installed", mode="after")
    def _year_not_in_future(cls, value: int, info: ValidationInfo):
        """
        Ensure that the year is not in the future.
        """
        current_year = date.today().year
        
        if value > current_year:
            raise ValueError(f"Year cannot be in the future (>{current_year})")
        
        return value
    
    @validator("state", mode="before")
    def _validate_state(cls, value, info: ValidationInfo):
        """
        Validate and convert the state to BoardState enum.
        """
        if isinstance(value, BoardState):
            return value
        
        if isinstance(value, str):
            val = value.strip().lower()
            try:
                return BoardState(val)
            except ValueError:
                valid_states = ", ".join([e.value for e in BoardState])
                raise ValueError(f"Invalid state '{value}'. Valid values: {valid_states}")
        raise ValueError("state must be a BoardState or str")
