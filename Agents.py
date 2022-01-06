from dataclasses import dataclass, fields
import datetime as dt

import requests

@dataclass
class Agents:
    """Agents class"""
    def __init__(self):
        id = 0
        api_model = ' '
        api_link = ' '
        title = ' '
        sort_title = ' '
        alt_titles = ' '
        birth_date = 0
        birth_place = ' '
        death_date = 0
        death_place = ' '
        description = ' '
        is_licensing_restricted = bool
        is_artist = bool
        agent_type_title = ' '
        agent_type_id = 0
        artwork_ids = 0
        site_ids = 0
        suggest_autocomplete_boosted = ' '
        suggest_autocomplete_all = ' '
        last_updated_source = dt.datetime
        last_updated = dt.datetime
        timestamp = dt.datetime

    id: int
    api_model: str
    api_link: str
    title: str
    sort_title: str
    alt_titles: str
    birth_date: int
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
    suggest_autocomplete_boosted: str
    suggest_autocomplete_all: str
    last_updated_source: dt.datetime
    last_updated: dt.datetime
    timestamp: dt.datetime

    def read(self, jsondata):
        status = 0
        dateformat = "%Y-%m-%dT%H:%M:%S%z"

        if(jsondata is not None):
            self.id = int(jsondata['id'])
            self.api_model = jsondata['api_model']
            self.api_link = jsondata['api_link']
            self.title = jsondata['title']
            self.sort_title = jsondata['sort_title']
            self.alt_titles = jsondata['alt_titles']
            if jsondata['birth_date'] == None:
                self.birth_date = 0
            else:
                self.birth_date = int(jsondata['birth_date'])
            self.birth_place = jsondata['birth_place']
            if jsondata['death_date'] == None:
                self.death_date = 0
            else:
                self.death_date = int(jsondata['death_date'])
            self.death_place = jsondata['death_place']
            self.description = jsondata['description']
            self.is_licensing_restricted = bool(jsondata['is_licensing_restricted'])
            self.is_artist = bool(jsondata['is_artist'])
            self.agent_type_title = jsondata['agent_type_title']
            if jsondata['agent_type_id'] == None:
                self.agent_type_id = 0           
            else:
                self.agent_type_id = int(jsondata['agent_type_id'])
            if jsondata['artwork_ids'] == None:
                self.artwork_ids = 0
            else:
                self.artwork_ids = jsondata['artwork_ids']
            if jsondata['site_ids'] == None:
                self.site_ids = 0
            else:
                self.site_ids = jsondata['site_ids']
            if jsondata.get('suggest_autocomplete_boosted') == None:
                self.suggest_autocomplete_boosted = ' '
            else:
                self.suggest_autocomplete_boosted = jsondata['suggest_autocomplete_boosted']
            if jsondata.get('suggest_autocomplete_all') == None:
                self.suggest_autocomplete_all = ' '
            else:
                self.suggest_autocomplete_all = jsondata['suggest_autocomplete_all']
            self.last_updated_source = dt.datetime.strptime(jsondata['last_updated_source'], dateformat)
            if jsondata.get('last_updated') == None:
                self.last_updated = dt.datetime(1970, 1, 1)
            else:
                self.last_updated = dt.datetime.strptime(jsondata['last_updated'], dateformat)
            self.timestamp = dt.datetime.strptime(jsondata['timestamp'], dateformat)
        else:
            status = -1

        return status

    def __str__(self):
        return self.title