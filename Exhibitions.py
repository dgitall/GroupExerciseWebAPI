from abc import abstractproperty
from dataclasses import dataclass, fields
import datetime as dt

import requests

@dataclass
class Exhibitions:
    """Exhibitions class"""
    def __init__(self):
        id = 0
        api_model = ''
        api_link = ''
        title = ''
        is_featured = bool
        description = ''
        short_description = ''
        web_url = ''
        image_url = ''
        type = ''
        status = ''
        aic_start_at = dt.datetime(1970, 1, 1)
        aic_end_at = dt.datetime(1970, 1, 1)
        date_display = ''
        department_display = ''
        gallery_id = 0
        gallery_title = ''
        artwork_ids = []
        artwork_titles = []
        artist_ids = []
        site_ids = []
        image_id: 0
        alt_image_ids = []
        document_ids = []
        ##suggest_autocomplete_boosted: object
        ##suggest_autocomplete_all: object
        last_updated_source = dt.datetime(1970, 1, 1)
        last_update = dt.datetime(1970, 1, 1)
        timestamp = dt.datetime(1970, 1, 1)
    
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
    
    def read(self, jsondata): 
        status = 0
        dateformat = "%Y-%m-%dT%H:%M:%S%z"
        if(jsondata is not None):
            self.id = int(jsondata['id'])
            self.api_model = jsondata['api_model']
            self.api_link = jsondata['api_link']
            self.title = jsondata['title']
            self.is_featured = bool(jsondata['is_featured'])
            self.description = jsondata['description']
            self.short_description = jsondata['short_description']
            self.web_url = jsondata['web_url']
            self.image_url = jsondata['image_url']
            self.type = jsondata ['type']
            self.aic_start_at = dt.datetime.strptime(jsondata['aic_start_at'], dateformat)
            self.aic_end_at = dt.datetime.strptime(jsondata['aic_end_at'], dateformat)
            self.date_display = jsondata['date_display']
            self.department_display = jsondata['department_display']
            self.gallery_id = jsondata['gallery_id']
            self.gallery_title = jsondata['gallery_title']
            self.artist_ids = jsondata['artist_ids']
            self.site_ids = jsondata['site_ids']
            self.image_id = jsondata['image_id']
            self.alt_image_ids = jsondata['alt_image_ids']
            self.document_ids = jsondata['document_ids']
            if jsondata.get('suggest_autocomplete_boosted') == None:
                self.suggest_autocomplete_boosted = ' '
            else:
                self.suggest_autocomplete_boosted = jsondata['suggest_autocomplete_boosted']
            if jsondata.get('suggest_autocomplete_all') == None:
                self.suggest_autocomplete_all = ' '
            else:
                self.suggest_autocomplete_all = jsondata['suggest_autocomplete_all']
            self.last_updated_source = dt.datetime.strptime(jsondata['last_updated_source'], dateformat)
            self.last_updated = dt.datetime.strptime(jsondata['last_updated'], dateformat)
            self.timestamp = dt.datetime.strptime(jsondata['timestamp'], dateformat)
        else:
            status = -1
                       
        return status
    
    def __str__(self):
        return self.title
    
    
    