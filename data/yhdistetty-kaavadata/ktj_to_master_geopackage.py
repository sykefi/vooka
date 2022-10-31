# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 13:11:38 2022

@author: smassine
"""

def setupMasterDataframe():
    
    import geopandas as gpd
    
    master_df = gpd.GeoDataFrame(columns=["geometry", "originalref", "vanhakuntakoodi", "kuntakoodi", "kuntanimi", "kaavatunnus_1", "kaavatunnus_2", "kaavaselite", "kaavalaji",
                                          "hyvaksymispvm", "vahvistamispvm", "voimaantulopvm", "kohderekisteriyksikot", "kaavakartta", "maaraykset", "selostus"],
                                 geometry="geometry", crs={'init': 'epsg:3067'})
    return(master_df)

def appendKTJToMaster(masterdf, ktjdata, geometry, originalref=None, kohderekisteriyksikot=None):
    
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
    
    # Etelä-Savon kuntakoodit
    kuntakoodit = {'Enonkoski':'046', 'Hirvensalmi':'097', 'Juva':'178', 'Kangasniemi':'213', 'Mikkeli':'491', 'Mäntyharju':'507', 'Pertunmaa':'588', 'Pieksämäki':'593', 'Puumala':'623', 'Rantasalmi':'681', 'Savonlinna':'740', 'Sulkava':'768'}
    
    i = 1
    
    for index, row in ktj_copy.iterrows():
        
        print("Processing " + str(i) + "/" + str(len(ktj_copy)))
        
        # Vanha kuntakoodi
        for key, item in enumerate(kuntakoodit):
            if kuntakoodit[item][0:3] == row['kaavatunnuksenkuntanumero']:
                vanhakuntakoodi = None
                break
            else:
                vanhakuntakoodi = row['kaavatunnuksenkuntanumero']
       
        # Kunnan nimi
        for key, item in enumerate(kuntakoodit):
            if kuntakoodit[item][0:3] == row['validkuntanro']:
                kuntanimi = item
                break
            else:
                kuntanimi = None
        
        # Kaavalaji
        if row['kayttorajoitusalalaji'] == 2001:
            kaavalaji = 21
        elif row['kayttorajoitusalalaji'] == 2103:
            kaavalaji = 33
        elif row['kayttorajoitusalalaji'] == 2102:
            kaavalaji = 39
        elif row['kayttorajoitusalalaji'] == 2101:
            kaavalaji = 31
        # 2150
        else:
            kaavalaji = None
            
        row_schema = {"geometry": row[geometry], "originalref": originalref, "vanhakuntakoodi": vanhakuntakoodi ,"kuntakoodi": row['validkuntanro'], "kuntanimi": kuntanimi, "kaavatunnus_1": row['yksilointitunnus'], "kaavatunnus_2": row['osannumero'],
                      "kaavaselite":row['nimi'], "kaavalaji": kaavalaji, "hyvaksymispvm": row['hyvaksymispvmvahvistamispvm'], "vahvistamispvm":None, "voimaantulopvm": row['voimaantulopvm'], "kohderekisteriyksikot": row[parameter_dict['kohderekisteriyksikot']],
                      "kaavakartta":None, "maaraykset":None, "selostus":None}
        
        masterdf = masterdf.append(row_schema, ignore_index=True)
        
        i = i + 1
        
    return(masterdf)

## Example
import geopandas as gpd
import pickle
from analyysi.kiinteistotunnus_to_kaavaindex import kiinteistotunnusToKaavaIndex
from funktiot.accessory_functions import saveGPKG

# KTJ data
ktj = gpd.read_file(r"<insert filepath here>")
#kunta = ktj.loc[ktj['validkuntanro'] == '<insert kuntanro here>']

# Kohderekisteriyksiköt
with open(r"<insert filepath here>.pkl", "rb") as f:
    kiinttunnukset = pickle.load(f)
kunta_data = kiinteistotunnusToKaavaIndex(kiinttunnus_data=kiinttunnukset, kaava_data=ktj)

# Prosessointi
master_df = setupMasterDataframe() # Korvaa "kaavat_processed" ensimmäisen appendin jälkeen!
kaavat_processed = appendKTJToMaster(masterdf=master_df, ktjdata=ktj, geometry='geometry')

"""
asemakaavat = [31, 32, 33, 34, 35, 39]
yleiskaavat = [21, 22, 23, 24, 25, 26]

asema = master_df.loc[master_df['kaavalaji'].isin(asemakaavat)]
yleis = master_df.loc[master_df['kaavalaji'].isin(yleiskaavat)]
saveGPKG(asema, outputfp=r"<insert filepath here>.gpkg", layer_name="<insert layer name here>")
saveGPKG(yleis, outputfp=r"<insert filepath here>.gpkg", layer_name="<insert layer name here>")
"""

saveGPKG(kaavat_processed, outputfp=r"<insert filepath here>.gpkg", layer_name="<insert layer name here>")