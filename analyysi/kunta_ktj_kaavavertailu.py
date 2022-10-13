# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 09:47:07 2022

@author: smassine
"""
import sys
from de9im_functions import get_DE9IM_pattern, topologically_equal_DE9IM, calculate_iou
from accessory_functions import setupMasterGDF, appendDataToMaster, saveGPKG

import geopandas as gpd

#import warnings
#warnings.filterwarnings("ignore")

def compareKuntadataToKTJ(kunta_data, ktj_data, kuntanimi, kaavalajit, dissolve_kunta, **kwargs):
    
    dissolve_column = kwargs.get('dissolve_column', None)

    kunta_pala = kunta_data.loc[kunta_data['kuntanimi'] == kuntanimi]
    kunta_pala = kunta_pala.loc[kunta_pala['kaavalaji'].isin(kaavalajit)]
    ktj_pala = ktj_data.loc[ktj_data['kuntanimi'] == kuntanimi]
    ktj_pala = ktj_pala.loc[ktj_pala['kaavalaji'].isin(kaavalajit)]
    
    # Check to see if datasets have the same CRS system
    if kunta_pala.crs['init'] != ktj_pala.crs['init']:
        # If not, comparison cannot be made. Sys exit.
        sys.exit("Your data must have the same coordinate reference system!")
    
    if dissolve_kunta == True:
        kunta_pala = kunta_pala.dissolve(by=dissolve_column)
        kunta_pala.reset_index(inplace=True)
    
    kunta_pala['area_ha'] = None
    kunta_pala['ktj_area_ha'] = None
    kunta_pala['de9im_pattern'] = None
    kunta_pala['topo_equal'] = None
    kunta_pala['iou'] = None
    kunta_pala['ktj_kaavatunnus'] = None
    kunta_pala['a_delta_%'] = None
    
    ktj_grouped = ktj_pala.groupby('kaavatunnus_1')
    
    for idx, row in kunta_pala.iterrows():
            
        geom1 = row['geometry']
        kunta_pala.at[idx, 'area_ha'] = geom1.area / 10000
        item_dict = {"knro":[], "iou":[], "pattern": [], "topo_equal": [], "ktj_area": [], "a_delta": []}
        print("---------")
        
        for key, value in ktj_grouped:
            
            kaava = value.dissolve(by='kaavatunnus_1')
            geom2 = kaava.at[kaava.index[0], 'geometry']
            
            if geom1.intersects(geom2) == True:
                iou = calculate_iou(geom1, geom2)
                print(iou)
                pattern = get_DE9IM_pattern(geom1, geom2)
                topo_equal = topologically_equal_DE9IM(geom1, geom2)
                ktj_area = geom2.area / 10000
                try:
                    delta = round(((ktj_area - (geom1.area / 10000)) / (geom1.area / 10000)) * 100, 2)
                except TypeError:
                    delta = None
                
                item_dict['knro'].append(str(kaava.index[0]))
                item_dict['iou'].append(iou)
                item_dict['pattern'].append(pattern)
                item_dict['topo_equal'].append(topo_equal)
                item_dict['ktj_area'].append(ktj_area)
                item_dict['a_delta'].append(delta)
        
        if len(item_dict['iou']) >= 1:
            kunta_pala.at[idx, 'iou'] = max(item_dict['iou'])
            indeksimme = item_dict['iou'].index(max(item_dict['iou']))
            kunta_pala.at[idx, 'ktj_kaavatunnus'] = item_dict['knro'][indeksimme]
            kunta_pala.at[idx, 'topo_equal'] = item_dict['topo_equal'][indeksimme]
            kunta_pala.at[idx, 'de9im_pattern'] = item_dict['pattern'][indeksimme]
            kunta_pala.at[idx, 'ktj_area_ha'] = item_dict['ktj_area'][indeksimme]
            kunta_pala.at[idx, 'a_delta_%'] = item_dict['a_delta'][indeksimme]
        else:
            None
    
    #List missing KTj indices
    lista = kunta_pala['ktj_kaavatunnus'].tolist()
    puuttuvat = []
    
    for index, row in ktj_pala.iterrows():
        
        if row['kaavatunnus_1'] not in lista:
            puuttuvat.append(row['kaavatunnus_1'])    
    
    print("")
    print("Missing KTJ indices:")
    print(sorted(set(puuttuvat)))
    
    return(kunta_pala)

kunta_data = gpd.read_file(r"<insert filepath here>.gpkg", layer="<insert layer name here>")
ktj_data = gpd.read_file(r"<insert filepath here>.gpkg", layer="<insert layer name here>")

# Esimerkki
results = compareKuntadataToKTJ(kunta_data=kunta_data, ktj_data=ktj_data, kuntanimi='Sulkava', kaavalajit=['33'], dissolve_kunta=True, dissolve_column='kaavatunnus')

master = setupMasterGDF(data=results, geom_column='geometry')
master_appended = appendDataToMaster(master_data=master, append_data=results)

saveGPKG(master_appended, outputfp=r"<insert filepath here>", layer_name="<insert layer name here>")