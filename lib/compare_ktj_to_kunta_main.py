
import sys
import geopandas as gpd
from shapely.geometry import Polygon, LineString, Point, MultiPolygon , MultiLineString, MultiPoint
import difflib
import pandas as pd

import warnings
warnings.filterwarnings("ignore")

from lib.compare_ktj_to_kunta_functions import trim, compare_items, check_existence, check_equality, setupMasterGDF, appendDataToMaster, saveGPKG, compare_and_return_match, get_DE9IM_pattern, topologically_equal_DE9IM, calculate_iou, filter_data, check_CRS, initialize_columns, iou_and_delta_to_columns


def compareKTJindicesToKunta(base_kaavadata, refe_kaavadata, kuntanimi, kaavalajit, dissolve_refe=False, **kwargs):
    
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
        True if there is a need to group kaavaindex base_layer_rows to form a kaava.
        False if input data already has an individual kaava as a base_layer_row.
    dissolve_column
        When dissolve_kunta=True
        Name of the column to be used when dissolving the data.
    
    Output
    ------
    <gpd.GeoDataFrame>
        KTJ's kaavadata with comparison information included.
    """

    
    dissolve_column = kwargs.get('dissolve_column', None)
    
    
    base_layer = filter_data(base_kaavadata, kuntanimi, kaavalajit)
    refe_layer = filter_data(refe_kaavadata, kuntanimi, kaavalajit)
    

    check_CRS(base_layer, refe_layer)
    
    column_names = [
    'area_ha',
    'refe_area_ha',
    'de9im_pattern',
    'topo_equal',
    'iou',
    'refe_kaavatunnus',
    'a_delta_%',
    'kl_equal',
    'hyv_equal',
    'voim_equal'
]

    
    initialize_columns(base_layer, column_names, default_value=None)

    
    if dissolve_refe == True:
        refe_layer = refe_layer.dissolve(by=dissolve_column)
        refe_layer.reset_index(inplace=True)
    
    base_layer = base_layer.dissolve(by="kaavatunnus_1")
    base_layer.reset_index(inplace=True)
    
    for index, base_layer_row in base_layer.iterrows():
        
        geom_base_layer = base_layer_row['geometry']
        base_layer.at[index, 'area_ha'] = geom_base_layer.area / 10000
        item_dict = {"kvnro":[], "iou":[], "pattern": [], "topo_equal": [], "refe_area": [], "a_delta": [], "kl_equal": [], "hyv_equal": [], "voim_equal": [], "false_a_delta": []}
        print("---------")
        
        for idx, refe_layer_row in refe_layer.iterrows():
            
            
            geom_refe_layer = refe_layer_row['geometry']
            
            
            if geom_base_layer.intersects(geom_refe_layer) == True:
                
                #Calculate DE9IM-pattern, iou-number, delta value, reference layer area
                pattern, iou, topo_equal, delta, refe_area = iou_and_delta_to_columns(geom_base_layer, geom_refe_layer)
                
                #Catch false posivite a_delta values
                if delta > 100:
                    possible_false_value = 1
                else:
                    possible_false_value = 0

                #See if kaavalaji is equal among base and reference
                kl_equal = check_equality(base_layer_row['kaavalaji'], refe_layer_row['kaavalaji'])
                
                #See if hyväksymispäivämäärä is equal among base and reference
                hyv_equal = None
                
                
                
                result_hyv = compare_items(base_layer_row['hyvaksymispvm'], refe_layer_row['hyvaksymispvm'])
                if result_hyv == True:
                    trimmed_refe_layer_row =  trim(refe_layer_row['hyvaksymispvm'])
                    if "x" in trimmed_refe_layer_row:
                        hyv_equal = 0
                    else:
                        hyv_equal = compare_and_return_match(base_layer_row['hyvaksymispvm'], trimmed_refe_layer_row)
                else:
                    hyv_equal = result_hyv

                
                #See if voimaantulopäivämäärä is equal among base and reference
                voim_equal = None
                result_voim = compare_items(base_layer_row['voimaantulopvm'], refe_layer_row['voimaantulopvm'])
                if result_voim == True:
                    trimmed_refe_layer_row =  trim(refe_layer_row['voimaantulopvm'])
                    if "x" in trimmed_refe_layer_row:
                        hyv_equal = 0
                    else:
                        voim_equal = hyv_equal = compare_and_return_match(base_layer_row['voimaantulopvm'], trimmed_refe_layer_row)
                else:
                    voim_equal = result_voim
                
                item_dict['kvnro'].append(refe_layer_row['kaavatunnus'])
                item_dict['iou'].append(iou)
                item_dict['pattern'].append(pattern)
                item_dict['topo_equal'].append(topo_equal)
                item_dict['refe_area'].append(refe_area)
                item_dict['a_delta'].append(delta)
                item_dict['kl_equal'].append(kl_equal)
                item_dict['hyv_equal'].append(hyv_equal)
                item_dict['voim_equal'].append(voim_equal)
                item_dict['false_a_delta'].append(possible_false_value)

        if len(item_dict['iou']) >= 1:
            base_layer.at[index, 'iou'] = max(item_dict['iou'])
            iou_max_value_at_index = item_dict['iou'].index(max(item_dict['iou']))
            base_layer.at[index, 'refe_kaavatunnus'] = item_dict['kvnro'][iou_max_value_at_index]
            base_layer.at[index, 'topo_equal'] = item_dict['topo_equal'][iou_max_value_at_index]
            base_layer.at[index, 'de9im_pattern'] = item_dict['pattern'][iou_max_value_at_index]
            base_layer.at[index, 'refe_area_ha'] = item_dict['refe_area'][iou_max_value_at_index]
            base_layer.at[index, 'a_delta_%'] = item_dict['a_delta'][iou_max_value_at_index]
            base_layer.at[index, 'kl_equal'] = item_dict['kl_equal'][iou_max_value_at_index]
            base_layer.at[index, 'hyv_equal'] = item_dict['hyv_equal'][iou_max_value_at_index]
            base_layer.at[index, 'voim_equal'] = item_dict['voim_equal'][iou_max_value_at_index]
            base_layer.at[index, 'false_a_delta'] = item_dict['false_a_delta'][iou_max_value_at_index]
        else:
            None
    
    #List missing reference indices
    lista = base_layer['refe_kaavatunnus'].tolist()
    puuttuvat = []
    
    for index, base_layer_row in refe_layer.iterrows():
        
        if base_layer_row['kaavatunnus'] not in lista:
            puuttuvat.append(base_layer_row['kaavatunnus'])    
    
    print("")
    print("Missing reference indices:")
    print(sorted(set(puuttuvat)))

    #print(base_layer)
    #base_exp = base_layer.explode()
    #base_exp = base_exp.reset_index(drop=True)
    print(base_layer)

    return(base_layer)


#Toimi
