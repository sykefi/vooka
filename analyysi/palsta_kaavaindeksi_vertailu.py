# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 10:46:48 2022

@author: smassine
"""
import geopandas as gpd
import sys

def calculateIntersectionPercentage(kaava, kaava_nro_column, palstat):
    
    """
    A Function for calculating an intersection percentage for two Shapely Polygons.
    
    Parameters
    ----------
    kaava: <gpd.GeoDataFrane>
        Yleis- or asemakaava data. Serving as a mask for kiinteistöpalstat.
    kaava_nro_column: <str>
        Name of the column in kaava parameter that individualises each kaavaindex.
    palstat: <gpd.GeoDataFrane>
        Palsta data. Used to store calculated intersection percentages and kaavaindex information.
            
    Output
    ------
    <GeoDataFrame>
        Combined data as a geopandas GeoDataFrame.
    """    
    
    # Check to see if kaava and palstadata have the same CRS system
    if kaava.crs['init'] != palstat.crs['init']:
        # If not, comparison cannot be made. Sys exit.
        sys.exit("Your data must have the same coordinate reference system!")
    
    # Retrieve kaava bbox to use as a mask
    xmin, ymin, xmax, ymax = kaava.total_bounds
    # Clip kaavadata with bbox
    palstat_rajaus = palstat.cx[xmin:xmax, ymin:ymax]
    
    # Store kiinteistötunnus in an own columns
    palstat_rajaus['kiinttunnus'] = None
    
    for index, row in palstat_rajaus.iterrows():
        palstat_rajaus.at[index, 'kiinttunnus'] = row['properties']['kiinteistotunnus']
    
    # Drop unnecessary columns and create columns for storing intersection percentages and kaavaindex information
    palstat_rajaus_drop = palstat_rajaus.drop(columns=['type', 'id', 'properties'])
    palstat_rajaus_drop['iou_1'] = None
    palstat_rajaus_drop['knro_1'] = None
    palstat_rajaus_drop['iou_2'] = None
    palstat_rajaus_drop['knro_2'] = None
    
    # Group data by kiinteistötunnus
    grouped = palstat_rajaus_drop.groupby('kiinttunnus')

    # Loop through each kiinteistötunnus in palstadata and see if the geometry intersects with kaavaindex
    # Store intersection percentages and kaavaindex information
    i = 1
    
    for key, value in grouped:
            
        print("Processing " + str(i) + "/" + str(len(grouped)))
        
        for index, row in value.iterrows():
            item_dict = {"knro":[], "iou":[]}
            
            for idx, rivi in kaava.iterrows():
                    
                if row['geometry'].intersects(rivi['geometry']) == True:
                    intersection_per = round((row['geometry'].intersection(rivi['geometry']).area / row['geometry'].area)*100, 2)
                    item_dict['knro'].append(str(rivi[kaava_nro_column]))
                    item_dict['iou'].append(intersection_per)
                    
            if len(item_dict['iou']) == 1:
                grouped.obj.at[index, 'iou_1'] = max(item_dict['iou'])
                indeksimme = item_dict['iou'].index(max(item_dict['iou']))
                grouped.obj.at[index, 'knro_1'] = item_dict['knro'][indeksimme]
                grouped.obj.at[index, 'iou_2'] = None
                grouped.obj.at[index, 'knro_2'] = None
                
            elif len(item_dict['iou']) > 1:
                grouped.obj.at[index, 'iou_1'] = max(item_dict['iou'])
                indeksimme = item_dict['iou'].index(max(item_dict['iou']))
                grouped.obj.at[index, 'knro_1'] = item_dict['knro'][indeksimme]
                
                item_dict['iou'].remove(max(item_dict['iou']))
                item_dict['knro'].remove(item_dict['knro'][indeksimme])
                grouped.obj.at[index, 'iou_2'] = max(item_dict['iou'])
                indeksimme = item_dict['iou'].index(max(item_dict['iou']))
                grouped.obj.at[index, 'knro_2'] = item_dict['knro'][indeksimme]
                
            else:
                grouped.obj.at[index, 'iou_1'] = 0
                grouped.obj.at[index, 'iou_2'] = None
                grouped.obj.at[index, 'knro_1'] = None
                grouped.obj.at[index, 'knro_2'] = None
                
        i = i + 1
    
    # Ungroup data
    intersection_shp = grouped.obj
    # Drop rows that didn't intersect with kaavadata
    intersection_shp_rajaus = intersection_shp.loc[intersection_shp['iou_1'] != 0.00]

    return(intersection_shp_rajaus)
