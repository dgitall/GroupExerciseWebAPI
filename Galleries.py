
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
        #suggest_autocomplete_boosted = ' '
        #suggest_autocomplete_all = ' '
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
    #suggest_autocomplete_boosted: str
    #suggest_autocomplete_all: str
    last_updated_source: dt.datetime
    last_updated: dt.datetime
    timestamp: dt.datetime
    
    # Possible functions
    # __str__ to return the title of the gallery
    # Read(jsondata) to pull out the values from the json data
    #       set the values in the class object
    
    def read(self, jsondata): 
        status = 0
        
        if(jsondata is not None):
            self.id = jsondata['id']
            self.api_model = jsondata['api_model']
            self.api_link = jsondata['api_link']
            self.title = jsondata['title']
            self.type = jsondata['type']
            self.is_closed = jsondata['is_closed']
            self.number = jsondata['number']
            self.floor = jsondata['floor']
            self.latitude = jsondata['latitude']
            self.longitude = jsondata['longitude']
            self.latlon = jsondata['latlon']
            self.last_updated_source = jsondata['last_updated_source']
            self.last_updated = jsondata['last_updated']
            self.timestamp = jsondata['timestamp']
        else:
            status = -1
                       
        return status
    
    def __str__(self):
        return title
    