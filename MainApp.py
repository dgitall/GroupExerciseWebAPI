## Main application file for the AIC API group project
import requests
from pprintpp import pprint as pp

import Galleries
import Places

baseURL = "https://api.artic.edu/api/v1/"
limitURL = "?limit=10"
pageURL = "&page="

################################
## Galleries

galleries_list = []
totalpages = 1
page = 0
while page < totalpages:
    galleriesURL = f"{baseURL}galleries{limitURL}{pageURL}{page+1}"
    response = requests.get(galleriesURL)
    galleries_json = response.json()
    
    if totalpages == 1:
        totalpages = int(galleries_json['pagination']['total_pages'])
    
    # pull out the data package from the json payload
    # it returns an iterable list of
    data = galleries_json['data']
    
    for galleryData in data:
        gallery = Galleries.Galleries()
        result = gallery.read(galleryData)
        if (result == 0):
            galleries_list.append(gallery)
    
    page += 1
            
pp(galleries_list)
        
################################
## Places

galleries_list = []
totalpages = 1
page = 0
while page < totalpages:
    galleriesURL = f"{baseURL}places{limitURL}{pageURL}{page+1}"
    response = requests.get(galleriesURL)
    galleries_json = response.json()
    
    if totalpages == 1:
        totalpages = int(galleries_json['pagination']['total_pages'])
    
    # pull out the data package from the json payload
    # it returns an iterable list of
    data = galleries_json['data']
    
    for galleryData in data:
        gallery = Places.Places()
        result = gallery.read(galleryData)
        if (result == 0):
            galleries_list.append(gallery)
    
    page += 1
            
pp(galleries_list)