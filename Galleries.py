
from dataclasses import dataclass, fields
import datetime as dt

@dataclass
class Galleries:
    """ Galleries class"""
    def __init__(self):
        id = 0
        api_model = ' '
        api_link = ' '
        title = ' '
        type = ' '
        is_closed = False
        number = ' '
        floor = ' '
        latitude = 0
        longitude = 0
        latlon = ' '
        suggest_autocomplete_boosted = ' '
        suggest_autocomplete_all = ' '
        last_updated_source = dt.datetime(1970, 1, 1)
        last_updated = dt.datetime(1970, 1, 1)
        timestamp = dt.datetime(1970, 1, 1)
        
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
            self.type = jsondata['type']
            self.is_closed = bool(jsondata['is_closed'])
            self.number = jsondata['number']
            self.floor = jsondata['floor']
            if jsondata['latitude'] == None:
                self.latitude = -999999
            else:
                self.latitude = float(jsondata['latitude'])
            if jsondata['longitude'] == None:
                self.longitude = -999999
            else:
                self.longitude = float(jsondata['longitude'])
            self.latlon = jsondata['latlon']
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
    