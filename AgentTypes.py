from abc import abstractproperty
from dataclasses import dataclass, fields
import datetime as dt

import requests

@dataclass
class AgentTypes:
    """AgentTypes class"""
    def __init__(self):
        id: 0
        api_model: ''
        api_link: ''
        title: ''
        # suggest_autocomplete_boosted: float
        # suggest_autocomplete_all: float
        last_updated_source: dt.datetime(1970, 1, 1)
        last_updated: dt.datetime(1970, 1, 1)
        timestamp: dt.datetime(1970, 1, 1)

    id: int
    api_model: str
    api_link: str
    title: str
    # suggest_autocomplete_boosted: float
    # suggest_autocomplete_all: float
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
            self.last_updated_source = jsondata['last_updated_source']
            self.last_updated = jsondata['last_updated']
            self.timestamp = jsondata['timestamp']
        else:
            status = -1

        return status

    def __str__(self):
        return self.title