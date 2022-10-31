# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 16:30:04 2022

@author: smassine
"""

def setupMasterDataframe():
    
    import geopandas as gpd
    
    master_df = gpd.GeoDataFrame(columns=["geometry", "originalref", "kuntakoodi", "kuntanimi", "kaavatunnus", "kaavaselite", "kaavalaji", "hyvaksymispvm",
                                          "vahvistamispvm", "voimaantulopvm", "kohderekisteriyksikot", "kaavakartta", "maaraykset", "selostus"],
                                 geometry="geometry", crs={'init': 'epsg:3067'})
    return(master_df)

def appendKuntaToMaster(masterdf, kaavadata, kaavalaji, geometry, kuntakoodi, kuntanimi, originalref=None, kaavatunnus=None, kaavaselite=None, hyvaksymispvm=None, vahvistamispvm=None, voimaantulopvm=None, kohderekisteriyksikot=None, kaavakartta=None, maaraykset=None, selostus=None):
    
    """
    Mandatory parameters
    --------------------
    masterdf: <gpd.GeoDataFrame>
        Master dataframe. Can be an empty GeoDataFrame or including value rows.
    kaavadata: <gpd.GeoDataFrame>
        Input kaavadata as a Geopandas GeoDataFrame.
    kaavalaji: <str>
        Either "asemakaava" or "yleiskaava".
    geometry: <str>
        Data's geometry column name as a string value.
    kuntakoodi: <str>
        Kuntakoodi for the wanted municipality.
    kuntanimi: <str>
        Name of the wanted municipality.

    Optional parameters
    -------------------
    originalref: <str>
        Data's original coordinate reference systmen as an EPSG code. E.g. "epsg:3067"
    kaavatunnus: <str>
        Name of the column in kaavadata representing the parameter.
    kaavaselite: <str>
        Name of the column in kaavadata representing the parameter.
    hyvaksymispvm: <str>
        Name of the column in kaavadata representing the parameter.
    vahvistamispvm: <str>
        Name of the column in kaavadata representing the parameter.
    voimaantulopvm: <str>
        Name of the column in kaavadata representing the parameter.
    kohderekisteriyksiköt: <str>
        Name of the column in kaavadata representing the parameter.
    kaavakartta: <str>
        Name of the column in kaavadata representing the parameter.
    maaraykset: <str>
        Name of the column in kaavadata representing the parameter.
    selostus: <str>
        Name of the column in kaavadata representing the parameter.
    
    Output
    ------
    <gpd.GeoDataFrame>
        Master dataframe including input kaavadata.
    """
    
    import sys
    
    if originalref == None:
        try:
            if kaavadata.crs['init'] != 'epsg:3067':
                originalref = str(kaavadata.crs['init'])
                kaavadata = kaavadata.to_crs(epsg=3067)
            else:
                originalref = str(kaavadata.crs['init'])
        except KeyError:
            sys.exit("Check coordinate reference system in kaavadata! Key 'init' is required!")
    
    parameter_dict = locals()
    kaava_copy = kaavadata.copy()

    for key in parameter_dict:
        try:
            if parameter_dict[key] == None:
                kaava_copy[str(key)] = None
                parameter_dict[key] = str(key)
        except ValueError:
            None
        
    # Kaavalaji dictionary, based on: https://koodistot.suomi.fi/codescheme;registryCode=rytj;schemeCode=RY_Kaavalaji
    kaavalaji_dict = {"maakuntakaava":[11, 12], "yleiskaava":[21, 22, 23, 24, 25, 26], "asemakaava":[31, 32, 33, 34, 35, 39]}
    
    i = 1
    
    for index, row in kaava_copy.iterrows():
        
        print("Processing " + str(i) + "/" + str(len(kaava_copy)))
        
        if kaavalaji == 'asemakaava':
            if row[parameter_dict['kaavaselite']] == None:
                kaavalaji_nro = kaavalaji_dict['asemakaava'][0]
            elif type(row[parameter_dict['kaavaselite']]) == float:
                kaavalaji_nro = kaavalaji_dict['asemakaava'][0]
            elif 'vaiheasemakaav' in row[parameter_dict['kaavaselite']].lower():
                kaavalaji_nro = kaavalaji_dict['asemakaava'][1]
            elif 'ranta-asema' in row[parameter_dict['kaavaselite']].lower() or 'rantakaava' in row[parameter_dict['kaavaselite']].lower():
                kaavalaji_nro = kaavalaji_dict['asemakaava'][2]
            elif 'vaiheranta' in row[parameter_dict['kaavaselite']].lower():
                kaavalaji_nro = kaavalaji_dict['asemakaava'][3]
            elif 'maanalai' in row[parameter_dict['kaavaselite']].lower():
                kaavalaji_nro = kaavalaji_dict['asemakaava'][4]
            elif 'ohjeellinen' in row[parameter_dict['kaavaselite']].lower():
                kaavalaji_nro = kaavalaji_dict['asemakaava'][5]
            else:
                kaavalaji_nro = kaavalaji_dict['asemakaava'][0]
        elif kaavalaji == 'yleiskaava':
            if row[parameter_dict['kaavaselite']] == None:
                kaavalaji_nro = kaavalaji_dict['yleiskaava'][0]
            elif 'vaiheyleiskaav' in row[parameter_dict['kaavaselite']].lower():
                kaavalaji_nro = kaavalaji_dict['yleiskaava'][1]
            elif 'osayleiskaav' in row[parameter_dict['kaavaselite']].lower():
                kaavalaji_nro = kaavalaji_dict['yleiskaava'][2]
            elif 'yhteinen yleiskaava' in row[parameter_dict['kaavaselite']].lower():
                kaavalaji_nro = kaavalaji_dict['yleiskaava'][3]
            elif 'oikeusvaikutukset' in row[parameter_dict['kaavaselite']].lower():
                kaavalaji_nro = kaavalaji_dict['yleiskaava'][4]
            elif 'maanalai' in row[parameter_dict['kaavaselite']].lower():
                kaavalaji_nro = kaavalaji_dict['yleiskaava'][5]
            else:
                kaavalaji_nro = kaavalaji_dict['yleiskaava'][0]
        else:
            sys.exit("Your kaavalaji parameter must be either 'asemakaava' or 'yleiskaava'!")
            
        row_schema = {"geometry": row[parameter_dict['geometry']], "originalref": originalref, "kuntakoodi": kuntakoodi, "kuntanimi": kuntanimi, "kaavatunnus": row[parameter_dict['kaavatunnus']],"kaavaselite": row[parameter_dict['kaavaselite']],
                      "kaavalaji": kaavalaji_nro, "hyvaksymispvm": row[parameter_dict['hyvaksymispvm']], "vahvistamispvm": row[parameter_dict['vahvistamispvm']], "voimaantulopvm": row[parameter_dict['voimaantulopvm']],
                      "kohderekisteriyksikot": row[parameter_dict['kohderekisteriyksikot']], "kaavakartta": row[parameter_dict['kaavakartta']], "maaraykset": row[parameter_dict['maaraykset']], "selostus": row[parameter_dict['selostus']]}

        masterdf = masterdf.append(row_schema, ignore_index=True)
        
        i = i + 1
    
    return(masterdf)

## Example
import geopandas as gpd
import pickle
from analyysi.kiinteistotunnus_to_kaavaindex import kiinteistotunnusToKaavaIndex
from funktiot.accessory_functions import saveGPKG

# Kaavadata
kunta_kaavadata = gpd.read_file(r"<insert filepath here>")

# Kohderekisteriyksiköt
with open(r"<insert filepath here>.pkl", "rb") as f:
    kiinttunnukset = pickle.load(f)
kunta_data = kiinteistotunnusToKaavaIndex(kiinttunnus_data=kiinttunnukset, kaava_data=kunta_kaavadata)

# Prosessointi
master_df = setupMasterDataframe() # Korvaa "kaavat_processed" ensimmäisen appendin jälkeen!
kaavat_processed = appendKuntaToMaster(masterdf=master_df, kaavadata=kunta_kaavadata, kaavalaji='yleiskaava', geometry='geometry', kuntakoodi='097', kuntanimi='Hirvensalmi', kaavaselite='nimi', hyvaksymispvm='pvm')

saveGPKG(kaavat_processed, outputfp=r"<insert filepath here>.gpkg", layer_name="<insert layer name here>")
