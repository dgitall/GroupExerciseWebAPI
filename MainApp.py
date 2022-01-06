## Main application file for the AIC API group project
import requests
from pprintpp import pprint as pp

import Galleries
import Places
import Agents
import AgentTypes
import Exhibitions

baseURL = "https://api.artic.edu/api/v1/"
limitURL = "?limit=10"
pageURL = "&page="


def ReadData(urlString, dataclass):
    data_list = []
    totalpages = 1
    page = 0
    while page < totalpages:
        getURL = f"{baseURL}{urlString}{limitURL}{pageURL}{page+1}"
        response = requests.get(getURL)
        datajson = response.json()
        
        if totalpages == 1:
            totalpages = int(datajson['pagination']['total_pages'])
        
        # pull out the data package from the json payload
        # it returns an iterable list of
        data = datajson['data']
        
        for dataset in data:
            object = dataclass()
            result = object.read(dataset)
            if (result == 0):
                data_list.append(object)
        
        page += 1
        
    return data_list
   

################################
## Galleries
galleriesList = ReadData('galleries', Galleries.Galleries)         
pp(galleriesList)
      
################################
## Places
places_list = ReadData('places', Places.Places)         
pp(places_list)

################################
## Agents
agents_list = ReadData('agents', Agents.Agents)         
pp(agents_list)

################################
## Agent Types
agenttypes_list = ReadData('agent-types', AgentTypes.AgentTypes)         
pp(agenttypes_list)


################################
## Exhibitions
exhibitions_list = ReadData('exhibitions', Exhibitions.Exhibitions)         
pp(exhibitions_list)
