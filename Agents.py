from abc import abstractproperty
from dataclasses import dataclass, fields
import datetime as dt

@dataclass
class Agents:
    """Agents class"""
    id: int
    api_model: str
    api_link: str
    title: str
    sort_title: str
    alt_titles: list
    bith_date: int
    birth_place: str
    death_date: int
    death_place: str
    description: str
    is_licensing_restricted: bool
    is_artist: bool
    agent_type_title: str
    agent_type_id: int
    artwork_ids: list
    site_ids: list
    suggest_autocomplete_boosted: str
    suggest_autocomplete_all: object
    last_updated_source: dt.datetime
    last_updated: dt.datetime
    timestamp: dt.datetime