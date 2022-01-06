from abc import abstractproperty
from dataclasses import dataclass, fields
import datetime as dt

@dataclass
class AgentTypes:
    """AgentTypes class"""
    
    id: int
    api_model: str
    api_link: str
    suggest_autocomplete_boosted: float
    suggest_autocomplete_all: float
    last_updated_source: dt.datetime
    last_updated: dt.datetime
    timestamp: dt.datetime