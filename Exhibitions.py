from abc import abstractproperty
from dataclasses import dataclass, fields
import datetime as dt

@dataclass
class Exhibitions:
    """Exhibitions class"""
    
    id: int
    api_model: str
    api_link: str
    title: str
    is_featured: bool
    description: str
    short_description: str
    web_url: str
    image_url: str
    type: str
    status: str
    aic_start_at: dt.datetime
    aic_end_at: dt.datetime
    date_display: str
    department_display: str
    gallery_id: int
    gallery_title: str
    artwork_ids: list
    artwork_titles: list
    artist_ids: list
    site_ids: list
    image_id: int
    alt_image_ids: list
    document_ids: list
    suggest_autocomplete_boosted: object
    suggest_autocomplete_all: object
    last_updated_source: dt.datetime
    last_update: dt.datetime
    timestamp: dt.datetime
    
    
    