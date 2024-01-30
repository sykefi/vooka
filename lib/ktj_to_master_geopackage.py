# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 13:11:38 2022

@author: smassine
"""

def setupKTJMasterDataframe():
    
    import geopandas as gpd
    
    master_df = gpd.GeoDataFrame(columns=["geometry", "originalref", "kuntakoodi", "kuntanimi", "kaavatunnus_1", "kaavatunnus_2", "kaavaselite", "kaavalaji", "hyvaksymispvm", "vahvistamispvm", "voimaantulopvm", "arkistotunnus", "kohderekisteriyksikot", "kaavakartta", "maaraykset"],
                                 geometry="geometry", crs={'init': 'epsg:3067'})
    return(master_df)


def appendKTJToMaster(masterdf, ktjdata, geometry, originalref=None, kohderekisteriyksikot_column="None"):
    
    """
    Mandatory parameters
    --------------------
    master_df: <gpd.GeoDataFrame>
        Master dataframe. Can be an empty GeoDataFrame or including value rows.
    ktjdata: <gpd.GeoDataFrame>
        Input KTJ data as a Geopandas GeoDataFrame.
    geometry: <str>
        Data's geometry column name as a string value.

    Optional parameters
    -------------------
    originalref: <str>
        Data's original coordinate reference systmen as an EPSG code. E.g. "epsg:3067"
    kohderekisteriyksiköt: <str>
        Name of the column in processed KTJ data representing the parameter.
    
    Output
    ------
    <gpd.GeoDataFrame>
        Master dataframe including input KTJ data.
    """
    
    import sys
    
    if originalref == None:
        try:
            if ktjdata.crs['init'] != 'epsg:3067':
                originalref = str(ktjdata.crs['init'])
                ktjdata = ktjdata.to_crs(epsg=3067)
            else:
                originalref = str(ktjdata.crs['init'])
        except KeyError:
            sys.exit("Check coordinate reference system in kaavadata! Key 'init' is required!")
    
    parameter_dict = locals()
    ktj_copy = ktjdata.copy()

    for key in parameter_dict:
        try:
            if parameter_dict[key] == None:
                ktj_copy[str(key)] = None
                parameter_dict[key] = str(key)
        except ValueError:
            None
    
    # Etelä-Savon ja Pohjois-Savon kuntakoodit
    kuntakoodit = {'Enonkoski':'046', 'Hirvensalmi':'097', 'Juva':'178', 'Kangasniemi':'213', 'Mikkeli':'491', 'Mäntyharju':'507', 'Pertunmaa':'588', 'Pieksämäki':'593', 'Puumala':'623', 'Rantasalmi':'681', 'Savonlinna':'740', 'Sulkava':'768', 'Iisalmi':'140', 'Joroinen':'171', 'Kaavi':'204', 'Keitele':'239', 'Kiuruvesi':'263', 'Kuopio':'297', 'Lapinlahti':'402', 'Leppävirta':'420', 'Pielavesi':'595', 'Rautalampi':'686', 'Rautavaara':'687', 'Siilinjärvi':'749', 'Sonkajärvi':'762', 'Suonenjoki':'778', 'Tervo':'844', 'Tuusniemi':'857', 'Varkaus':'915', 'Vesanto':'921', 'Vieremä': '925'}
    
    i = 1
    
    for index, row in ktj_copy.iterrows():
        
        print("Processing " + str(i) + "/" + str(len(ktj_copy)))
        
        # Vanha kuntakoodi
        for key, item in enumerate(kuntakoodit):
            if kuntakoodit[item][0:3] == row['KAAVAKNRO']:
                vanhakuntakoodi = None
                break
            else:
                vanhakuntakoodi = row['KAAVAKNRO']
       
        # Kunnan nimi
        for key, item in enumerate(kuntakoodit):
            if kuntakoodit[item][0:3] == row['kuntakoodi']:
                kuntanimi = item
                break
            else:
                kuntanimi = None
        
        # Kaavalaji
        if row['KAYTRAJALA'] == 2001:
            kaavalaji = 21
        elif row['KAYTRAJALA'] == 2103:
            kaavalaji = 33
        elif row['KAYTRAJALA'] == 2102:
            kaavalaji = 39
        elif row['KAYTRAJALA'] == 2101:
            kaavalaji = 31
        # 2150, tarkentantamaton
        else:
            kaavalaji = None
        
        row_schema = {"geometry": row[geometry], "originalref": originalref, "kuntakoodi": row['kuntakoodi'], "kuntanimi": kuntanimi, "kaavatunnus_1": row['YKSILOINTI'], "kaavatunnus_2": row['OSANNUMERO'],
                      "kaavaselite":row['NIMI'], "kaavalaji": kaavalaji, "hyvaksymispvm": row['HYVAKPVM'], "vahvistamispvm": row['REKISTEROI'], "voimaantulopvm": row['VOIMAANPVM'], "arkistotunnus": row['ARKISTOTUN'], "kohderekisteriyksikot": row[kohderekisteriyksikot_column],
                      "kaavakartta":None, "maaraykset":None, "selostus":None}
        
        masterdf = masterdf.append(row_schema, ignore_index=True)
        
        i = i + 1
        
    return(masterdf)