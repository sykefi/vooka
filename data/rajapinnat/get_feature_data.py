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

# Some tests with Etelä-Savo ELY web services
#--------------------------------------------

# Rantasalmi WFS
# WORKING FINE!
getWFSlayers("https://kuntanetcloud01.cgisaas.fi/geoserver.g1/kuntanet_rantasalmi/wms")
data = getWFSdata("https://kuntanetcloud01.cgisaas.fi/geoserver.g1/kuntanet_rantasalmi/wms", "kuntanet_rantasalmi:MI_OSAYLEISKAAVARAJAT")

# Sulkava WFS
# WORKING FINE!
getWFSlayers("https://kunnat.navici.com/geoserver/sulkava/wfs")
"""
['sulkava:ajantasakaava_kaavarajat', 'sulkava:ajantasakaava_kaavarajat_preview',
 'sulkava:kaavarajat_osayleiskaava', 'sulkava:kaavarajat_osayleiskaava_preview']
"""
data = getWFSdata("https://kunnat.navici.com/geoserver/sulkava/wfs", "sulkava:ajantasakaava_kaavarajat")

# Mikkeli WFS
# WORKING FINE!
kunta = getArcgisFeatureLayer("https://services1.arcgis.com/biwBTnEqa75tyWMg/ArcGIS/rest/services/RAK_indeksi/FeatureServer/0")
