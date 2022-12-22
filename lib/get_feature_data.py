# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 10:34:24 2022

@author: smassine
"""

def getWFSlayers(url):
    
    from owslib.wfs import WebFeatureService
    
    # Initialize
    wfs = WebFeatureService(url=url)
    
    # Fetch all layers
    layers= list(wfs.contents)
    
    return(layers)
    
def getWFSdata(url, layer):
    
    from requests import Request
    import geopandas as gpd
    
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
    
    import esri2gpd
    
    # Read service to GeoDataFrame
    gdf = esri2gpd.get(layer_url)
    
    return(gdf)
