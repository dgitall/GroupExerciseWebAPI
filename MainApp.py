## Main application file for the AIC API group project
import requests
from pprintpp import pprint as pp

import Galleries
import Places
import Agents
import AgentTypes

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

################################
## Agents

agents_list = []
totalpages = 1
page = 0
while page < totalpages:
    agentsURL = f"{baseURL}agents{limitURL}{pageURL}{page+1}"
    response = requests.get(agentsURL)
    agents_json = response.json()
    
    if totalpages == 1:
        totalpages = int(agents_json['pagination']['total_pages'])
    
    # pull out the data package from the json payload
    # it returns an iterable list of
    data = agents_json['data']
    
    for agentData in data:
        agent = Agents.Agents()
        result = agent.read(agentData)
        if (result == 0):
            agents_list.append(agent)
    
    page += 1
            
pp(agents_list)

################################
## Agent Types

agenttypes_list = []
totalpages = 1
page = 0
while page < totalpages:
    agenttypesURL = f"{baseURL}agenttypes{limitURL}{pageURL}{page+1}"
    response = requests.get(agenttypesURL)
    agenttypes_json = response.json()
    
    if totalpages == 1:
        totalpages = int(agenttypes_json['pagination']['total_pages'])
    
    # pull out the data package from the json payload
    # it returns an iterable list of
    data = agenttypes_json['data']
    
    for agenttypeData in data:
        agenttype = AgentTypes.AgentTypes()
        result = agenttype.read(agenttypeData)
        if (result == 0):
            agenttypes_list.append(agenttype)
    
    page += 1
            
pp(agenttypes_list)
