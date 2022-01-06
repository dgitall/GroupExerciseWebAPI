
from dataclasses import dataclass, fields
import datetime as dt

@dataclass
class Galleries:
    """ Galleries class"""
    
    id: int
    api_model: str
    api_link: str
    title: str
    type: str
    is_closed: bool
    number: str
    floor: str
    latitude: float
    longitude: float
    latlon: str
    suggest_autocomplete_boosted: float
    suggest_autocomplete_all: float
    last_updated_source: dt.datetime
    last_updated: dt.datetime
    timestamp: dt.datetime
    
    # Possible functions
    # __init__ to take in all of the above parameters
    # __str__ to return the title of the gallery

    