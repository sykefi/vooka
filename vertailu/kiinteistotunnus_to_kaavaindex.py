# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 16:22:43 2022

@author: smassine
"""
import os
import geopandas as gpd
import pickle
from shapely.geometry import box

def kiinteistotunnusToKaavaIndex(kiinttunnus_data, kaava_data, outfp):

    """
    A Function for assigning kaavatunnus information to each kaavaindex.
    
    Parameters
    ----------
    kiinttunnus_data: <gpd.GeoDataFrane>
        Kiinteistötunnus data as a geopandas GeoDataFrame.
    kaava_data: <gpd.GeoDataFrane>
        Kaavadata as a geopandas GeoDataFrame.
    outfp: <str>
        Full output filepath with filename and output format (.shp). E.g. r"C:\Files\mikkeli_asemakaava_kiinteistotunnukset.shp" 
            
    Output
    ------
    <GeoDataFrame>
        Saved shp-file as a geopandas GeoDataFrame.
    """    

    # Define bbox for kiinteistotunnukset based on kaavadata
    bounds = kaava_data.total_bounds
    bbox = box(*bounds)
    
    # Clip kiinteistotunnukset data with bbox
    kiinttunnus_data['intersect'] = None
    
    i = 1
    
    for index, row in kiinttunnus_data.iterrows():
        
        print("Processing: " + str(i) + "/" + str(len(kiinttunnus_data)))
        
        if row['geometry'].intersects(bbox) == True:
            kiinttunnus_data.at[index, 'intersect'] = 'True'
        
        i = i + 1
        
    kunta_kiinttunnus = kiinttunnus_data.loc[kiinttunnus_data['intersect'] == 'True']
    kunta_kiinttunnus = kunta_kiinttunnus.drop(columns=['intersect'])
    
    # Loop through kaavaindexes and kiinteistötunnukset to see which kiinteistötunnukset are inside each kaavaindex
    kaava_data['kiinttunnus'] = None
    i = 1
    
    for index, row in kaava_data.iterrows():
        
        print("------------------------------------------------------")
        print("Processing: " + str(i) + "/" + str(len(kaava_data)))
        print("------------------------------------------------------")
        
        kaava = row
        kiinttunnus_list = []
        
        for idx, row in kunta_kiinttunnus.iterrows():
            
            if row['geometry'].within(kaava['geometry']):
                print("Kiinteistötunnus found within kaavaindex!")
                kiinttunnus_list.append(row.kiinteistotunnus)
        
        if len(kiinttunnus_list) != 0:
            kaava_data.at[index, 'kiinttunnus'] = str(kiinttunnus_list)
        
        i = i + 1
    
    # Save outfile
    # If file already exists, don't copy it again:
    if os.path.isfile(outfp) == True:
        print("")
        print(outfp, "already exists!")
    # If file doesn't already exist, create it
    else:
        print("")
        print("Saving file...")        
        kaava_data.to_file(outfp)
    
    return(kaava_data)
