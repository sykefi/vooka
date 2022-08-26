# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 10:46:48 2022

@author: smassine
"""
import geopandas as gpd
import sys
import os

def calculateIntersectionPercentage(kaava, kaava_nro_column, palstat, outfp):
    
    if kaava.crs['init'] != palstat.crs['init']:
        sys.exit("Your data must have the same coordinate reference system!")
    
    xmin, ymin, xmax, ymax = kaava.total_bounds
    palstat_rajaus = palstat.cx[xmin:xmax, ymin:ymax]

    palstat_rajaus['kiinttunnus'] = None
    
    for index, row in palstat_rajaus.iterrows():
        
        palstat_rajaus.at[index, 'kiinttunnus'] = row['properties']['kiinteistotunnus']

    palstat_rajaus_drop = palstat_rajaus.drop(columns=['type', 'id', 'properties'])
    palstat_rajaus_drop['iou_1'] = None
    palstat_rajaus_drop['knro_1'] = None
    palstat_rajaus_drop['iou_2'] = None
    palstat_rajaus_drop['knro_2'] = None
    grouped = palstat_rajaus_drop.groupby('kiinttunnus')

    i = 1

    for key, value in grouped:
            
        print("Processing " + str(i) + "/" + str(len(grouped)))
        
        for index, row in value.iterrows():

            item_dict = {"knro":[], "iou":[]}
            
            for idx, rivi in kaava.iterrows():
                    
                if row['geometry'].intersects(rivi['geometry']) == True:
                        
                    iou = round((row['geometry'].intersection(rivi['geometry']).area / row['geometry'].area)*100, 2)
                    item_dict['knro'].append(str(rivi[kaava_nro_column]))
                    item_dict['iou'].append(iou)
                    
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
            
    iou_shp = grouped.obj
    iou_shp_rajaus = iou_shp.loc[iou_shp['iou_1'] != 0.00]
    
    # Save outfile
    # If file already exists, don't copy it again:
    if os.path.isfile(outfp) == True:
        print("")
        print(outfp, "already exists!")
    # If file doesn't already exist, create it
    else:
        print("")
        print("Saving file...")        
        iou_shp_rajaus.to_file(outfp)

    return(iou_shp_rajaus)
