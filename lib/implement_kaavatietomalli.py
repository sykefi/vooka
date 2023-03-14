# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 13:23:18 2022

@author: smassine
"""

def dataToGeoJSON(kaavadata, aineistolahde, ktj_kaavatunnus, kunta_kaavatunnus):
    
    """
    A function for creating a GeoJSON file (collections.OrderedDict) from Geopandas GeoDataFrame.
    
    Parameters
    --------------------
    kaavadata: <gpd.GeoDataframe>
        Input kaavadata as a GeoPandas GeoDataFrame.
    aineistolahde: <str>
        Informs the data source. Either "KTJ" or "kunta".
    ktj_kaavatunnus: <str>
        KTJ-kaavatunnus column name as a string value.
    kunta_kaavatunnus: <str>
        Municipality's kaavatunnus column as a string value.
    
    Output
    ------
    <collections.OrderedDict>
        Output kaavadata as a Python OrderedDict (equivalent to JSON, can be saved as such).
    """    
    
    import json
    from collections import OrderedDict
    import sys
    import ast
    
    # Function to order GeoJSON keys properly
    def ordered(d, desired_key_order):
        return OrderedDict([(key, d[key]) for key in desired_key_order])
    
    # Storing columns to be dropped later
    col_list = kaavadata.columns
    col_list = col_list.drop('geometry')
    
    # Adding new columns based on kaavatietomalli
    # https://tietomallit.ymparisto.fi/kaavatiedot/v1.1/looginenmalli/uml/doc/
    new_columns = ["hallinnollinenAlue",
                   "nimi",
                   "kuvaus",
                   "asianhallintaTunnus",
                   "vireilletuloAika",
                   "elinkaaritila",
                   "aluerajaus",
                   "asianLiite",
                   "metatietokuvaus",
                   "diaarinumero",
                   "paikallinenTunnus",
                   "nimiavaruus",
                   "viittausTunnus",
                   "identiteettiTunnus",
                   "tuottajakohtainenTunnus",
                   "viimeisinMuutos",
                   "tallennusAika",
                   "kaavasuunnitelma"]
    
    for item in new_columns:
        kaavadata[item] = None
    
    # Copy kaavadata so we are not messing original data up
    kopio = kaavadata.copy()  
    
    # Iterate over kaavadata and change it to kaavatietomalli
    for index, row in kaavadata.iterrows():
        
        # Storages for tables
        hal_alue_lista = []
        hal_alue_dict = {"tunnus": row['kuntakoodi'],
                         "nimi": row['kuntanimi']}
        hal_alue_lista.append(hal_alue_dict)
        
        kaavasuun_lista = []
        kaavasuun_dict = {"laji": None,
                          "kaavaTunnus": None,
                          "kumoamistieto": None,
                          "digitaalinenAlkupera": "https://koodistot.suomi.fi/code;registryCode=rytj;schemeCode=RY_DigitaalinenAlkupera;codeCode=04",
                          "maanalaisuus": "https://koodistot.suomi.fi/code;registryCode=rytj;schemeCode=RY_MaanalaisuudenLaji;codeCode=02",
                          "oikeusvaikutteisuus": None,
                          "voimassaoloAika": None,
                          "alueellaSijaitsevaKiinteisto": None,
                          "kaavanKuvaus": None, 
                          "kaavanTeema": None,
                          "kaavakartta": None,
                          "mittakaava": None}
        
        # hallinnollineAlue
        kopio.at[index,"hallinnollinenAlue"] = hal_alue_lista
        
        # kuvaus
        if aineistolahde == "KTJ":
            kopio.at[index, "kuvaus"] = "Aluerajaus KTJ-aineistosta, asiakirjat kunnalta"
        elif aineistolahde == "kunta":
            kopio.at[index, "kuvaus"] = "Aluerajaus ja asiakirjat kunnalta"
        else:
            sys.exit("Your 'aineistolahde' parameter must be either 'KTJ' or 'kunta'!")
        
        # vireilletuloAika
        try:
            kopio.at[index, 'vireilletuloAika'] = row['hyvaksymispvm']
        except KeyError:
            None
        
        # elinkaaritila
        kopio.at[index, 'elinkaaritila'] = "https://koodistot.suomi.fi/code;registryCode=rytj;schemeCode=RY_KaavanElinkaaritila;codeCode=11"
        
        # asianLiite
        liite_lista = []
        
        kaavakartta_maar = row['kaavakartta_maar']
        kaavakartta = row['kaavakartta']
        maarays = row['maaraykset']
        selostus = row['selostus']
        oas = row['oas']
        muu = row['muu']
        
        # Kaavakartta sis. maar
        if kaavakartta_maar != None:
            apu_lista = kaavakartta_maar.split(", ")
            for item in apu_lista:
                liite_dict = {"asiakirjanTunnus": None,
                              "nimi": None,
                              "laji": None,
                              "lisatietolinkki": None,
                              "metatietokuvaus": None,
                              "asiakirjanJulkisuusluokka": None}
                liite_dict['nimi'] = str(item)
                liite_dict['laji'] = "https://koodistot.suomi.fi/code;registryCode=rytj;schemeCode=RY_AsiakirjanLaji_YKAK;codeCode=05"
                liite_dict['asiakirjanJulkisuusluokka'] = "https://koodistot.suomi.fi/code;registryCode=rytj;schemeCode=julkisuus;codeCode=1" #lähtökohtaisesti kaikki julkisia!
                liite_lista.append(liite_dict)
        
        # Kaavakartta
        if kaavakartta != None:
            apu_lista = kaavakartta.split(", ")
            for item in apu_lista:
                liite_dict = {"asiakirjanTunnus": None,
                              "nimi": None,
                              "laji": None,
                              "lisatietolinkki": None,
                              "metatietokuvaus": None,
                              "asiakirjanJulkisuusluokka": None}
                liite_dict['nimi'] = str(item)
                liite_dict['laji'] = "https://koodistot.suomi.fi/code;registryCode=rytj;schemeCode=RY_AsiakirjanLaji_YKAK;codeCode=03"
                liite_dict['asiakirjanJulkisuusluokka'] = "https://koodistot.suomi.fi/code;registryCode=rytj;schemeCode=julkisuus;codeCode=1" #lähtökohtaisesti kaikki julkisia!
                liite_lista.append(liite_dict)
        
        # Maaraykset
        if maarays != None:
            apu_lista = maarays.split(", ")
            for item in apu_lista:
                liite_dict = {"asiakirjanTunnus": None,
                              "nimi": None,
                              "laji": None,
                              "lisatietolinkki": None,
                              "metatietokuvaus": None,
                              "asiakirjanJulkisuusluokka": None}
                liite_dict['nimi'] = str(item)
                liite_dict['laji'] = "https://koodistot.suomi.fi/code;registryCode=rytj;schemeCode=RY_AsiakirjanLaji_YKAK;codeCode=04"
                liite_dict['asiakirjanJulkisuusluokka'] = "https://koodistot.suomi.fi/code;registryCode=rytj;schemeCode=julkisuus;codeCode=1" #lähtökohtaisesti kaikki julkisia!
                liite_lista.append(liite_dict)
       
        # Selostukset
        if selostus != None:
            apu_lista = selostus.split(", ")
            for item in apu_lista:
                liite_dict = {"asiakirjanTunnus": None,
                              "nimi": None,
                              "laji": None,
                              "lisatietolinkki": None,
                              "metatietokuvaus": None,
                              "asiakirjanJulkisuusluokka": None}
                liite_dict['nimi'] = str(item)
                liite_dict['laji'] = "https://koodistot.suomi.fi/code;registryCode=rytj;schemeCode=RY_AsiakirjanLaji_YKAK;codeCode=06"
                liite_dict['asiakirjanJulkisuusluokka'] = "https://koodistot.suomi.fi/code;registryCode=rytj;schemeCode=julkisuus;codeCode=1" #lähtökohtaisesti kaikki julkisia!
                liite_lista.append(liite_dict) 
        
        # OAS
        if oas != None:
            apu_lista = oas.split(", ")
            for item in apu_lista:
                liite_dict = {"asiakirjanTunnus": None,
                              "nimi": None,
                              "laji": None,
                              "lisatietolinkki": None,
                              "metatietokuvaus": None,
                              "asiakirjanJulkisuusluokka": None}
                liite_dict['nimi'] = str(item)
                liite_dict['laji'] = "https://koodistot.suomi.fi/code;registryCode=rytj;schemeCode=RY_AsiakirjanLaji_YKAK;codeCode=14"
                liite_dict['asiakirjanJulkisuusluokka'] = "https://koodistot.suomi.fi/code;registryCode=rytj;schemeCode=julkisuus;codeCode=1" #lähtökohtaisesti kaikki julkisia!
                liite_lista.append(liite_dict)
        
        # Muu
        if muu != None:
            apu_lista = muu.split(", ")
            for item in apu_lista:
                liite_dict = {"asiakirjanTunnus": None,
                              "nimi": None,
                              "laji": None,
                              "lisatietolinkki": None,
                              "metatietokuvaus": None,
                              "asiakirjanJulkisuusluokka": None}
                liite_dict['nimi'] = str(item)
                liite_dict['laji'] = "https://koodistot.suomi.fi/code;registryCode=rytj;schemeCode=RY_AsiakirjanLaji_YKAK;codeCode=99"
                liite_dict['asiakirjanJulkisuusluokka'] = "https://koodistot.suomi.fi/code;registryCode=rytj;schemeCode=julkisuus;codeCode=1" #lähtökohtaisesti kaikki julkisia!
                liite_lista.append(liite_dict)
       
        if len(liite_lista) == 0:
            liite_dict = {"asiakirjanTunnus": None,
                          "nimi": None,
                          "laji": None,
                          "lisatietolinkki": None,
                          "metatietokuvaus": None,
                          "asiakirjanJulkisuusluokka": None}
            liite_lista.append(liite_dict)
        
        kopio.at[index, 'asianLiite'] = liite_lista
        
        # paikallinenTunnus
        try:
            if type(row[kunta_kaavatunnus]) != None:
                kopio.at[index, 'paikallinenTunnus'] = row[kunta_kaavatunnus]
            else:
                None
        except KeyError:
            None

        # tuottajakohtainenTunnus
        try:
            if type(row[ktj_kaavatunnus]) != None:
                kopio.at[index, 'tuottajakohtainenTunnus'] = row[ktj_kaavatunnus]
            else:
                None
        except KeyError:
            None
        
        ## kaavasuunnitelma
        # kaavalaji
        if row['kaavalaji'] == '21':
            kaavasuun_dict["laji"] = "http://uri.suomi.fi/codelist/rytj/RY_Kaavalaji/code/23"
        else:
            kaavasuun_dict["laji"] = "http://uri.suomi.fi/codelist/rytj/RY_Kaavalaji/code/" + row['kaavalaji']
        
        # oikeusvaikutteisuus
        if row['kaavalaji'] != '25':
            kaavasuun_dict["oikeusvaikutteisuus"] = "https://koodistot.suomi.fi/code;registryCode=rytj;schemeCode=RY_OikeusvaikutteisuudenLaji;codeCode=01"
        else:
            kaavasuun_dict["oikeusvaikutteisuus"] = "https://koodistot.suomi.fi/code;registryCode=rytj;schemeCode=RY_OikeusvaikutteisuudenLaji;codeCode=02"
            
        # alueellaSijaitsevaKiinteisto
        kiinteisto_lista = []
        if row['kohderekisteriyksikot'] != None:
            tunnus_lista = ast.literal_eval(row['kohderekisteriyksikot'])
            for item in tunnus_lista:
                kiinteisto_dict = {"kiinteistoTunnus": None,
                                   "sisaltyyKokonaan": None,
                                   "sisaltyvaPintala": None}
                kiinteisto_dict['kiinteistoTunnus'] = item
                kiinteisto_lista.append(kiinteisto_dict)
        else:
            kiinteisto_dict = {"kiinteistoTunnus": None,
                               "sisaltyyKokonaan": None,
                               "sisaltyvaPintala": None}
            kiinteisto_lista.append(kiinteisto_dict)
        
        kaavasuun_dict['alueellaSijaitsevaKiinteisto'] = kiinteisto_lista
        
        # kaavanKuvaus
        try:
            if len(row['kaavaselite']) > 0:
                kaavasuun_dict["kaavanKuvaus"] = row['kaavaselite']
            else:
                None
        except TypeError:
            None
            
        kaavasuun_lista.append(kaavasuun_dict)
        kopio.at[index, 'kaavasuunnitelma'] = kaavasuun_lista
    
    # Drop unnecessary columns
    kopio = kopio.drop(col_list, axis=1)
    
    # Pandas to GeoJSON
    geojson = kopio.to_json()
    json_data = json.loads(geojson)
    
    # Add general infromation
    json_data['name'] = 'VOOKA-etelasavo'
    json_data['crs'] = {"type": "name", "properties": {"name": "urn:ogc:def:crs:EPSG::3067"}}
    
    # Set GeoJSON keys in proper order    
    entity_desired_key_order = ('type', 'name', 'crs', 'features')
    result = ordered(json_data, entity_desired_key_order)
    
    return(result)


def jsonToGPKG(inputfp, outputfp):
    
    """
    A function for creating and saving a geopackage file from JSON data.
    
    Parameters
    --------------------
    inputfp: <str>
        Full input filepath to JSON data file.
    outputfp: <str>
        Full output filepath for newly created gpkg-file.
    
    Output
    ------
    <gpd.GeoDataFrame>
        Saved gpkg-file as a GeoPandas GeoDataFrame.
    """    
    
    import pandas as pd
    import geopandas as gpd
    import json
    from shapely.geometry import Polygon, MultiPolygon
    from fiona.crs import from_epsg
    
    # Read data
    with open(inputfp, encoding='utf8') as json_file:
        data = json.load(json_file)
    
    # Focusing on features
    df = pd.json_normalize(data['features'])
    
    # Normalize constant keys (dicts)
    df_halue = df['properties.hallinnollinenAlue'].explode().apply(pd.Series)
    df_halue.rename(columns={col:f'hallinnollinenAlue.{col}' for col in df_halue.columns}, inplace=True)
    
    df_ksuun = df['properties.kaavasuunnitelma'].explode().apply(pd.Series)
    df_ksuun.rename(columns={col:f'kaavasuunnitelma.{col}' for col in df_ksuun.columns}, inplace=True)
    
    cols = [col for col in df.columns if col not in ['properties.hallinnollinenAlue', 'properties.kaavasuunnitelma']]
    df_uusi = df[cols].join(df_halue).join(df_ksuun)
    
    # Create column for Shapely geometry creation
    df_uusi['geometry'] = None
    
    kopio = df_uusi.copy()
    
    # Iterate over data and create geometries
    for index, row in df_uusi.iterrows():
        
        if row['geometry.type'] == 'Polygon':
            kopio.at[index, 'geometry'] = Polygon(row['geometry.coordinates'][0])
            
        elif row['geometry.type'] == 'MultiPolygon':
            
            polygon_list = []
            
            for i in row['geometry.coordinates']:
                geom = Polygon(i[0])
                polygon_list.append(geom)
                
            kopio.at[index, 'geometry'] = MultiPolygon(polygon_list)
            
        else:
            None
    
    # Create GeoDataFrame
    gdf = gpd.GeoDataFrame(kopio, geometry='geometry')
    
    # Set upcolumns to normalize kaavaliite information
    kopio = gdf.copy()
    kopio['asianLiite.kaavakartta'] = None
    kopio['asianLiite.kaavakarttaJaMaaraykset'] = None
    kopio['asianLiite.maaraykset'] = None
    kopio['asianLiite.selostus'] = None
    kopio['asianLiite.oas'] = None
    kopio['asianLiite.muu'] = None
    kopio['asianLiite.asiakirjanJulkisuusluokka'] = None
    
    # Normalize kaavaliite information
    for index, row in gdf.iterrows():
        
        item_dict = {"kaavakartta_sis_maar":[], "kaavakartta":[], "maaraykset": [], "selostus": [], "oas": [], "muu": []}
        
        if len(row['properties.asianLiite']) == 1 and row['properties.asianLiite'][0]['nimi'] == None:
            None
        else:
            for item in row['properties.asianLiite']:
                
                if kopio.at[index, 'asianLiite.asiakirjanJulkisuusluokka'] == None:
                    kopio.at[index, 'asianLiite.asiakirjanJulkisuusluokka'] = item['asiakirjanJulkisuusluokka']
                else:
                    None
                
                if item['nimi'][7:9] == '03':
                    item_dict['kaavakartta'].append(item['nimi'])
                elif item['nimi'][7:9] == '05':
                    item_dict['kaavakartta_sis_maar'].append(item['nimi'])
                elif item['nimi'][7:9] == '04':
                    item_dict['maaraykset'].append(item['nimi'])
                elif item['nimi'][7:9] == '06':
                    item_dict['selostus'].append(item['nimi'])
                elif item['nimi'][7:9] == '14':
                    item_dict['oas'].append(item['nimi'])
                elif item['nimi'][7:9] == '99':
                    item_dict['muu'].append(item['nimi'])
                else:
                    None
            
            if len(item_dict['kaavakartta']) == 0:
                None
            else:
                kaavakartat = ', '.join(item_dict['kaavakartta'])
                kopio.at[index, 'asianLiite.kaavakartta'] = kaavakartat
                
            if len(item_dict['kaavakartta_sis_maar']) == 0:
                None
            else:
                kartat_ja_maaraykset = ', '.join(item_dict['kaavakartta_sis_maar'])
                kopio.at[index, 'asianLiite.kaavakarttaJaMaaraykset'] = kartat_ja_maaraykset
                
            if len(item_dict['maaraykset']) == 0:
                None
            else:
                maaraykset = ', '.join(item_dict['maaraykset'])
                kopio.at[index, 'asianLiite.maaraykset'] = maaraykset
                
            if len(item_dict['selostus']) == 0:
                None
            else:
                selostukset = ', '.join(item_dict['selostus'])
                kopio.at[index, 'asianLiite.selostus'] = selostukset
                
            if len(item_dict['oas']) == 0:
                None
            else:
                oas = ', '.join(item_dict['oas'])
                kopio.at[index, 'asianLiite.oas'] = oas
            
            if len(item_dict['muu']) == 0:
                None
            else:
                muut = ', '.join(item_dict['muu'])
                kopio.at[index, 'asianLiite.muu'] = muut
    
        if len(row['kaavasuunnitelma.alueellaSijaitsevaKiinteisto']) == 1 and row['kaavasuunnitelma.alueellaSijaitsevaKiinteisto'][0]['kiinteistoTunnus'] == None:
            kopio.at[index, 'kaavasuunnitelma.alueellaSijaitsevaKiinteisto'] = None
        else:
            tunnus_list = []
            for item in row['kaavasuunnitelma.alueellaSijaitsevaKiinteisto']:
                tunnus_list.append(item['kiinteistoTunnus'])
            tunnus_str = ', '.join(tunnus_list)
            kopio.at[index, 'kaavasuunnitelma.alueellaSijaitsevaKiinteisto'] = tunnus_str
    
    # Drop unnecessary columns
    result = kopio.drop(columns=['geometry.coordinates', 'id', 'properties.asianLiite'])
    # Setup TM35 FIN as coordinate reference system
    result.crs = from_epsg(3067)
    # Save file
    result.to_file(outputfp, driver="GPKG")

    return(result)
