import svgwrite
import numpy as np
import json
import xml.etree.ElementTree as ET
 

PATH_MAP = "/home/abeldm3108/Github/abeldonate.github.io/content/map/"
PATH_MD = "/home/abeldm3108/Github/abeldonate.github.io/content/map/"
PATH_JSON = "/home/abeldm3108/Github/abeldonate.github.io/content/map/"

COLOR_VISITED = "#ff0000"
COLOR_NOT_VISITED = "#d3d2d1"

HEADER = """
+++
title = "Map"
render = true
template = "about.html"
+++

A map with all the countries I have visited

![Caption](./map/FinalMap.svg)

"""


#Read the json file
with open(PATH_JSON + 'countries.json', 'r') as f:
    data = json.load(f)
N = len(data["countries"])


#Add the countries in the markdown list
with open(PATH_MD + 'index.md', 'w') as f:
    f.write(HEADER)
    for i in range(N):
        strike = ""
        if(data["countries"][i]["visited"]):
            strike = "~~"
        f.write("- " + strike + data["countries"][i]["country"] + strike +"\n")


#Color the map
tree = ET.parse(PATH_MAP + "Map.svg")
root = tree.getroot()

for child in root[0]:
    #print(child.tag, child.attrib)
    countryId = child.get('id')
    if len(countryId)==2:
        #print(countryId) 
        for i in range(N):
            if data["countries"][i]["id"] == countryId:
                print(countryId)
                if data["countries"][i]["visited"]:
                    child.set('style', 'fill:' + COLOR_VISITED) 
                else:
                    child.set('style', 'fill:' + COLOR_NOT_VISITED) 
                break

tree.write(PATH_MAP + 'FinalMap.svg')
