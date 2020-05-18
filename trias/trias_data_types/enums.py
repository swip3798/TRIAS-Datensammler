from enum import Enum

class PtMode(Enum):
    '''
    Enumeration for all vehicle types
    '''
    ALL = "all"
    UNKNOWN = "unknown"
    AIR = "air"
    BUS = "bus"
    TROLLEYBUS = "trolleyBus"
    TRAM = "tram"
    COACH = "coach"
    RAIL = "rail"
    INTERCITYRAIL = "intercityRail"
    URBANRAIL = "urbanRail"
    METRO = "metro"
    WATER = "water"
    CABLEWAY = "cableway"
    FUNICULAR = "funicular"
    TAXI = "taxi"

class LineDirection(Enum):
    '''
    Enumeration for possible directions for lines
    '''
    FORTH = 1
    BACK = 2

class StopEventType(Enum):
    '''
    For StopEventRequest, possible types of StopEvents
    '''
    DEPARTURE = "departure" 
    ARRIVAL = "arrival" 
    BOTH = "both"