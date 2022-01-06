from abc import abstractproperty
from dataclasses import dataclass, fields
import datetime as dt

@dataclass
class Places:
    """Places class"""
    
    id: int
    api_model: str
    api_link: str
    title: str
    suggest_autocomplete_boosted: object
    suggest_autocomplete_all: object
    last_updated_source: dt.datetime
    last_update: dt.datetime
    timestamp: dt.datetime