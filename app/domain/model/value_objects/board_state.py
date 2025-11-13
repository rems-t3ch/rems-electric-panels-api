from enum import Enum

"""
Represents the state of a board in the system.

Attributes:
    OPERATIVE (str): The board is functioning normally.
    MAINTENANCE (str): The board is under maintenance.
    OUT_OF_SERVICE (str): The board is out of service.
"""
class BoardState(str, Enum):
    OPERATIVE = "operative"
    MAINTENANCE = "maintenance"
    OUT_OF_SERVICE = "out_of_service"