from enum import Enum

"""
Represents the state of a panel in the system.

Attributes:
    OPERATIVE (str): The panel is functioning normally.
    MAINTENANCE (str): The panel is under maintenance.
    OUT_OF_SERVICE (str): The panel is out of service.
"""
class PanelState(str, Enum):
    OPERATIVE = "operative"
    MAINTENANCE = "maintenance"
    OUT_OF_SERVICE = "out_of_service"
