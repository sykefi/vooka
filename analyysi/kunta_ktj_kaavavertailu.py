# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 09:47:07 2022

@author: smassine
"""
import sys
from funktiot.de9im_functions import get_DE9IM_pattern, topologically_equal_DE9IM, calculate_iou
from funktiot.accessory_functions import setupMasterGDF, appendDataToMaster, saveGPKG
import geopandas as gpd

#import warnings
#warnings.filterwarnings("ignore")

def compareKuntadataToKTJ(kunta_data, ktj_data, kuntanimi, kaavalajit, dissolve_kunta=False, **kwargs):
    
    """
    Mandatory parameters
    --------------------
    kunta_data: <gpd.GeoDataFrame>
        Input kaavadata from municipalities as a Geopandas Geodataframe.
    ktj_data: <gpd.GeoDataFrame>
        Input KTJ-data from MML as a Geopandas Geodataframe.
    kuntanimi: <str>
        Name of the wanted municipality.
    kaavalajit <list>, list item <str>
        A list including kaavalaji numbers to be examined. E.g. asemakaavat ['31', '33']
        Check all numbers from: https://koodistot.suomi.fi/codescheme;registryCode=rytj;schemeCode=RY_Kaavalaji

    Optional parameters
    -------------------
    dissolve_kunta <boolean>
        True/False (default False).
        True if there is a need to group kaavaindex rows to form a kaava.
        False if input data already has an individual kaava as a row.
    dissolve_column
        When dissolve_kunta=True
        Name of the column to be used when dissolving the data.
    
    Output
    ------
    <gpd.GeoDataFrame>
        Municipality's kaavadata with comparison information included.
    """
    
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
                if topo_equal == False:
                    if iou >= 98:
                        topo_equal = True
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

def compareKTJdataToKunta(base_kaavadata, refe_kaavadata, kuntanimi, kaavalajit, dissolve_refe=False, **kwargs):
    
    """
    Mandatory parameters
    --------------------
    base_kaavadata: <gpd.GeoDataFrame>
        Input kaavadata as a Geopandas Geodataframe, KTJ from MML in this case. To be used as a base for comparisons.
    refe_kaavadata: <gpd.GeoDataFrame>
        Input reference data from municipalities as a Geopandas Geodataframe.
    kuntanimi: <str>
        Name of the wanted municipality.
    kaavalajit <list>, list item <str>
        A list including kaavalaji numbers to be examined. E.g. asemakaavat ['31', '33']
        Check all numbers from: https://koodistot.suomi.fi/codescheme;registryCode=rytj;schemeCode=RY_Kaavalaji

    Optional parameters
    -------------------
    dissolve_refe <boolean>
        True/False (default False).
        True if there is a need to group kaavaindex rows to form a kaava.
        False if input data already has an individual kaava as a row.
    dissolve_column
        When dissolve_kunta=True
        Name of the column to be used when dissolving the data.
    
    Output
    ------
    <gpd.GeoDataFrame>
        KTJ's kaavadata with comparison information included.
    """
    
    dissolve_column = kwargs.get('dissolve_column', None)
    
    base_pala = base_kaavadata.loc[base_kaavadata['kuntanimi'] == kuntanimi]
    base_pala = base_pala.loc[base_pala['kaavalaji'].isin(kaavalajit)]
    refe_pala = refe_kaavadata.loc[refe_kaavadata['kuntanimi'] == kuntanimi]
    refe_pala = refe_pala.loc[refe_pala['kaavalaji'].isin(kaavalajit)]
    
    # Check to see if datasets have the same CRS system
    if base_pala.crs['init'] != refe_pala.crs['init']:
        # If not, comparison cannot be made. Sys exit.
        sys.exit("Your data must have the same coordinate reference system!")
    
    base_pala['area_ha'] = None
    base_pala['refe_area_ha'] = None
    base_pala['de9im_pattern'] = None
    base_pala['topo_equal'] = None
    base_pala['iou'] = None
    base_pala['refe_kaavatunnus'] = None
    base_pala['a_delta_%'] = None
    
    if dissolve_refe == True:
        refe_pala = refe_pala.dissolve(by=dissolve_column)
        refe_pala.reset_index(inplace=True)
    
    base_pala = base_pala.dissolve(by="kaavatunnus_1")
    base_pala.reset_index(inplace=True)
    
    for index, row in base_pala.iterrows():
        
        geom1 = row['geometry']
        base_pala.at[index, 'area_ha'] = geom1.area / 10000
        item_dict = {"knro":[], "iou":[], "pattern": [], "topo_equal": [], "refe_area": [], "a_delta": []}
        print("---------")
        
        for idx, rivi in refe_pala.iterrows():
                
            geom2 = rivi['geometry']
                
            if geom1.intersects(geom2) == True:
                iou = calculate_iou(geom1, geom2)
                print(iou)
                pattern = get_DE9IM_pattern(geom1, geom2)
                topo_equal = topologically_equal_DE9IM(geom1, geom2)
                if topo_equal == False:
                    if iou >= 98:
                        topo_equal = True
                refe_area = geom2.area / 10000
                try:
                    delta = round(((refe_area - (geom1.area / 10000)) / (geom1.area / 10000)) * 100, 2)
                except TypeError:
                    delta = None
                
                item_dict['knro'].append(rivi['kaavatunnus'])
                item_dict['iou'].append(iou)
                item_dict['pattern'].append(pattern)
                item_dict['topo_equal'].append(topo_equal)
                item_dict['refe_area'].append(refe_area)
                item_dict['a_delta'].append(delta)
        
        if len(item_dict['iou']) >= 1:
            base_pala.at[index, 'iou'] = max(item_dict['iou'])
            indeksimme = item_dict['iou'].index(max(item_dict['iou']))
            base_pala.at[index, 'refe_kaavatunnus'] = item_dict['knro'][indeksimme]
            base_pala.at[index, 'topo_equal'] = item_dict['topo_equal'][indeksimme]
            base_pala.at[index, 'de9im_pattern'] = item_dict['pattern'][indeksimme]
            base_pala.at[index, 'refe_area_ha'] = item_dict['refe_area'][indeksimme]
            base_pala.at[index, 'a_delta_%'] = item_dict['a_delta'][indeksimme]
        else:
            None
    
    #List missing reference indices
    lista = base_pala['refe_kaavatunnus'].tolist()
    puuttuvat = []
    
    for index, row in refe_pala.iterrows():
        
        if row['kaavatunnus'] not in lista:
            puuttuvat.append(row['kaavatunnus'])    
    
    print("")
    print("Missing reference indices:")
    print(sorted(set(puuttuvat)))
    
    base_exp = base_pala.explode()
    base_exp = base_exp.reset_index(drop=True)
    
    return(base_exp)

kunta_data = gpd.read_file(r"<insert filepath here>.gpkg", layer="<insert layer name here>")
ktj_data = gpd.read_file(r"<insert filepath here>.gpkg", layer="<insert layer name here>")

# Example
results = compareKuntadataToKTJ(kunta_data=kunta_data, ktj_data=ktj_data, kuntanimi='Sulkava', kaavalajit=['31', '39'], dissolve_kunta=True, dissolve_column='kaavatunnus')
results2 = compareKTJdataToKunta(base_kaavadata=ktj_data, refe_kaavadata=kunta_data, kuntanimi='Kangasniemi', kaavalajit=['33'])

master = setupMasterGDF(data=results, geom_column='geometry')

try:
    master_appended = appendDataToMaster(master_data=master, append_data=results)
except SystemExit:
    results = results[list(master.columns)]
    master_appended = appendDataToMaster(master_data=master, append_data=results)

saveGPKG(master_appended, outputfp=r"<insert filepath here>", layer_name="<insert layer name here>")
