from abc import abstractproperty
from dataclasses import dataclass, fields
import datetime as dt

import requests

@dataclass
class Agents:
    """Agents class"""
    def __init__(self):
        id: 0
        api_model: ''
        api_link: ''
        title: ''
        sort_title: ''
        alt_titles: 0
        bith_date: 0
        birth_place: ''
        death_date: 0
        death_place: ''
        description: ''
        is_licensing_restricted: bool
        is_artist: bool
        agent_type_title: ''
        agent_type_id: 0
        artwork_ids: 0
        site_ids: 0
        # suggest_autocomplete_boosted: str
        # suggest_autocomplete_all: object
        last_updated_source: dt.datetime
        last_updated: dt.datetime
        timestamp: dt.datetime

    id: int
    api_model: str
    api_link: str
    title: str
    sort_title: str
    alt_titles: float
    bith_date: int
    birth_place: str
    death_date: int
    death_place: str
    description: str
    is_licensing_restricted: bool
    is_artist: bool
    agent_type_title: str
    agent_type_id: int
    artwork_ids: float
    site_ids: float
    # suggest_autocomplete_boosted: str
    # suggest_autocomplete_all: object
    last_updated_source: dt.datetime
    last_updated: dt.datetime
    timestamp: dt.datetime

    def read(self, jsondata):
        status = 0

        if(jsondata is not None):
            self.id = jsondata['id']
            self.api_model = jsondata['api_model']
            self.api_link = jsondata['api_link']
            self.title = jsondata['title']
            self.sort_title = jsondata['sort_title']
            self.alt_titles = jsondata['alt_titles']
            self.bith_date = jsondata['birth_date']
            self.birth_place = jsondata['birth_place']
            self.death_date = jsondata['death_date']
            self.death_place = jsondata['death_place']
            self.description = jsondata['description']
            self.is_licensing_restricted = jsondata['is_licensing_restricted']
            self.is_artist = jsondata['is_artist']
            self.agent_type_title = jsondata['agent_type_title']
            self.agent_type_id = jsondata['agent_type_id']
            self.artwork_ids = jsondata['artwork_ids']
            self.site_ids = jsondata['site_ids']
            self.last_updated_source = jsondata['last_updated_source']
            self.last_updated = jsondata['last_updated']
            self.timestamp = jsondata['timestamp']
        else:
            status = -1

        return status

    def __str__(self):
        return self.title