# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 16:42:00 2022

@author: smassine
"""

import os
import requests
import xmltodict
from shapely.geometry import Polygon
import geopandas as gpd

def pieksamakiAsemakaavaToSHP(outfp):
    
    """
    A Function for parsing Pieksämäki WFS KuntaGML to geopandas GeoDataFrame and saving a shapefile.
    
    Parameter
    ----------
    outfp: <str>
        Full output filepath with filename and output format. E.g. r"C:\Files\pieksamaki_asemakaava.shp"
    
    Output
    ------
    <GeoDataFrame>
        Saved shp-file as a geopandas GeoDataFrame.
    """
    
    # Connect to Pieksämäki WFS
    url = "https://kartat.pieksamaki.fi/teklaogcweb/WFS.ashx?service=WFS&request=getfeature&typename=akaava:Kaava"
    response = requests.get(url)
    data = xmltodict.parse(response.content)
    
    # Set up GeoDataFrame for the shp-file
    dataframe = gpd.GeoDataFrame(columns = ['kieli', 'kaavatunnus', 'muukaavatunnus', 'arkistotunnus',
           'kaavanimi', 'kaavanlaatija', 'hyvaksyja', 'hyvaksymispvm', 'kuntakoodi', 'kaavanvaihe',
           'kaavatyyppi', 'liitteet', 'historiatiedot', 'mittakaava', 'kaavamaarayskirjasto', 'geometry'])
    
    # Set up coordinate reference system
    dataframe.crs = {'init' :'epsg:3067'}
    
    # Loop through each asemakaava
    pituus = len(data['wfs:FeatureCollection']['gml:featureMember'])
    i = 0
    
    for i in range(pituus - 1):
    
        pala = data['wfs:FeatureCollection']['gml:featureMember'][i]
    
        list1 = pala['akaava:Kaava']['akaava:kieli1']
        list2 = pala['akaava:Kaava']['akaava:kaavatunnus']
        list3 = pala['akaava:Kaava']['akaava:muuKaavatunnus']
        list4 = pala['akaava:Kaava']['akaava:arkistotunnus']
        list5 = pala['akaava:Kaava']['akaava:kaavanimi1']
        list6 = pala['akaava:Kaava']['akaava:kaavanlaatija']
        list7 = pala['akaava:Kaava']['akaava:hyvaksyja']
        list8 = pala['akaava:Kaava']['akaava:hyvaksymispvm']
        list9 = pala['akaava:Kaava']['akaava:kuntakoodi']
        list10 = pala['akaava:Kaava']['akaava:kaavanvaihe']
        list11 = pala['akaava:Kaava']['akaava:kaavatyyppi']
        
        try:
            list12 = pala['akaava:Kaava']['akaava:liitteet']['akaava:Liite']['@linkki']
        except TypeError:
            list12 = 'Ei liitteitä'
            
        list13 = pala['akaava:Kaava']['akaava:historiatiedot']
        list14 = pala['akaava:Kaava']['akaava:teknisetTiedot']['akaava:TekninenTieto']['akaava:mittakaava']
        list15 = pala['akaava:Kaava']['akaava:kaavamaarayskirjasto']
        
        try:
            a_list = pala['akaava:Kaava']['akaava:voimassaolosijainti']['gml:Polygon']['gml:outerBoundaryIs']['gml:LinearRing']['gml:coordinates'].split()
            res = [eval(x) for x in a_list]
        
            list16 = Polygon(res)
        
        except KeyError:
            print("")
            print('Ei geometriaa, ei tallenneta mukana:')
            print(pala)
            
        yhd = {'kieli': list1, 'kaavatunnus': list2, 'muukaavatunnus': list3, 'arkistotunnus': list4,
               'kaavanimi': list5, 'kaavanlaatija': list6, 'hyvaksyja': list7, 'hyvaksymispvm': list8,
               'kuntakoodi': list9, 'kaavanvaihe': list10, 'kaavatyyppi': list11, 'liitteet': list12,
               'historiatiedot': list13, 'mittakaava': list14, 'kaavamaarayskirjasto': list15, 'geometry': list16}
            
        dataframe = dataframe.append(yhd, ignore_index=True)
        
        i = i + 1
    
    # If file already exists, don't copy it again:
    if os.path.isfile(outfp) == True:
        print("")
        print(outfp, "on jo olemassa!")
    # If file doesn't already exist, create it
    else:
        print("")
        print("Tallennetaan shp-tiedosto...")        
        # Save asemakaava
        dataframe.to_file(outfp)
    
    return(dataframe)
