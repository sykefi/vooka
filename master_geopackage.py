# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 10:12:44 2022

@author: smassine
"""

from kiinteistotunnus_to_kaavaindex import kiinteistotunnusToKaavaIndex

import geopandas as gpd
import pickle

# Setting up the master dataframe schema
master_df = gpd.GeoDataFrame(columns=["geometry", "originalref", "kuntakoodi", "kuntanimi", "kaavatunnus", "kaavaselite", "kaavalaji", "hyvaksymispvm",
                                      "vahvistamispvm", "voimaantulopvm", "kohderekisteriyksikot", "kaavakartta", "maaraykset", "selostus"],
                             geometry="geometry", crs={'init': 'epsg:3067'})

# Kaavalaji dictionary, based on: https://koodistot.suomi.fi/codescheme;registryCode=rytj;schemeCode=RY_Kaavalaji
kaavalaji_dict = {"maakuntakaava":[11, 12], "yleiskaava":[21, 22, 23, 24, 25, 26], "asemakaava":[31, 32, 33, 34, 35, 39]}

def appendAsemakaavaToMaster(masterdf, kaavadata, geometry, originalref, kuntakoodi, kuntanimi, kaavatunnus, kaavaselite, hyvaksymispvm, vahvistamispvm, voimaantulopvm, kohderekisteriyksikot, kaavakartta, maaraykset, selostus):
    
    i = 1
    
    for index, row in kaavadata.iterrows():
        
        print("Processing " + str(i) + "/" + str(len(kaavadata)))
        
        if row[kaavaselite] == None:
            kaavalaji = kaavalaji_dict['asemakaava'][0]
        elif 'vaiheasemakaav' in row[kaavaselite].lower():
            kaavalaji = kaavalaji_dict['asemakaava'][1]
        elif 'ranta-asema' in row[kaavaselite].lower() or 'rantakaava' in row[kaavaselite].lower():
            kaavalaji = kaavalaji_dict['asemakaava'][2]
        elif 'vaiheranta' in row[kaavaselite].lower():
            kaavalaji = kaavalaji_dict['asemakaava'][3]
        elif 'maanalai' in row[kaavaselite].lower():
            kaavalaji = kaavalaji_dict['asemakaava'][4]
        elif 'ohjeellinen' in row[kaavaselite].lower():
            kaavalaji = kaavalaji_dict['asemakaava'][5]
        else:
            kaavalaji = kaavalaji_dict['asemakaava'][0]
        
        row_schema = {"geometry": row[geometry], "originalref": originalref, "kuntakoodi": kuntakoodi, "kuntanimi": kuntanimi, "kaavatunnus": row[kaavatunnus],"kaavaselite":row[kaavaselite],
        "kaavalaji": kaavalaji, "hyvaksymispvm": row[hyvaksymispvm], "vahvistamispvm": vahvistamispvm, "voimaantulopvm": voimaantulopvm, "kohderekisteriyksikot": row[kohderekisteriyksikot],
        "kaavakartta": row[kaavakartta], "maaraykset": row[maaraykset], "selostus": selostus}
        
        masterdf = masterdf.append(row_schema, ignore_index=True)
        i = i + 1
        
    return(masterdf)

def appendYleiskaavaToMaster(masterdf, kaavadata, geometry, originalref, kuntakoodi, kuntanimi, kaavatunnus, kaavaselite, hyvaksymispvm, vahvistamispvm, voimaantulopvm, kohderekisteriyksikot, kaavakartta, maaraykset, selostus):
    
    i = 1
    
    for index, row in kaavadata.iterrows():
        
        print("Processing " + str(i) + "/" + str(len(kaavadata)))
        
        if row[kaavaselite] == None:
            kaavalaji = kaavalaji_dict['yleiskaava'][0]
        elif 'vaiheyleiskaav' in row[kaavaselite].lower():
            kaavalaji = kaavalaji_dict['yleiskaava'][1]
        elif 'osayleiskaav' in row[kaavaselite].lower():
            kaavalaji = kaavalaji_dict['yleiskaava'][2]
        elif 'yhteinen yleiskaava' in row[kaavaselite].lower():
            kaavalaji = kaavalaji_dict['yleiskaava'][3]
        elif 'oikeusvaikutukset' in row[kaavaselite].lower():
            kaavalaji = kaavalaji_dict['yleiskaava'][4]
        elif 'maanalai' in row[kaavaselite].lower():
            kaavalaji = kaavalaji_dict['yleiskaava'][5]
        else:
            kaavalaji = kaavalaji_dict['yleiskaava'][0]
    
        row_schema = {"geometry": row[geometry], "originalref": originalref, "kuntakoodi": kuntakoodi, "kuntanimi": kuntanimi, "kaavatunnus": kaavatunnus,"kaavaselite":row[kaavaselite],
        "kaavalaji": kaavalaji, "hyvaksymispvm": row[hyvaksymispvm], "vahvistamispvm": vahvistamispvm, "voimaantulopvm": voimaantulopvm, "kohderekisteriyksikot": row[kohderekisteriyksikot],
        "kaavakartta": kaavakartta, "maaraykset": row[maaraykset], "selostus": selostus}
        
        masterdf = masterdf.append(row_schema, ignore_index=True)
        i = i + 1
        
    return(masterdf)

