# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 10:34:24 2022

@author: smassine
"""
import geopandas as gpd
from requests import Request
from owslib.wfs import WebFeatureService
import esri2gpd

def getWFSlayers(url):
    
    # Initialize
    wfs = WebFeatureService(url=url)
    
    # Fetch all layers
    layers= list(wfs.contents)
    
    return(layers)
    
def getWFSdata(url, layer):
    
    # Get data from WFS
    # -----------------
    
    # Specify the parameters for fetching the data
    params = dict(service='WFS', version="2.0.0", request='GetFeature', typeName=layer)
    
    # Parse the URL with parameters
    q = Request('GET', url, params=params).prepare().url

    # Read data from URL
    data = gpd.read_file(q)  
    
    return(data)

def getArcgisFeatureLayer(layer_url):
    
    # Read service to GeoDataFrame
    gdf = esri2gpd.get(layer_url)
    
    return(gdf)
