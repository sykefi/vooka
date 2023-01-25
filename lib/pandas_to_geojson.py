# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 13:23:18 2022

@author: smassine
"""

def dataToGeoJSON(kaavadata, kaavatunnus_col):
    
    import ast
    
    # Function to order GeoJSON keys properly
    def ordered(d, desired_key_order):
        return OrderedDict([(key, d[key]) for key in desired_key_order])
    
    # Storing columns to be dropped later
    col_list = kaavadata.columns
    col_list = col_list.drop('geometry')
    
    # Adding new columns based on kaavatietomalli
    # https://tietomallit.ymparisto.fi/kaavatiedot/v1.1/looginenmalli/uml/doc/
    new_columns = ["laji",
                   "kaavaTunnus",
                   "kumoamistieto",
                   "digitaalinenAlkupera",
                   "maanalaisuus",
                   "oikeusvaikutteisuus",
                   "voimassaoloAika",
                   "alueellaSijaitsevaKiinteisto",
                   "nimi",
                   "kuvaus",
                   "asianhallintaTunnus",
                   "vireilletuloAika",
                   "elinkaaritila",
                   "asianLiite",
                   "aluerajaus",
                   "metatietokuvaus",
                   "paikallinenTunnus",
                   "nimiavaruus",
                   "viittausTunnus",
                   "identiteettiTunnus",
                   "tuottajakohtainenTunnus",
                   "viimeisinMuutos",
                   "tallennusAika"]
    
    for item in new_columns:
        kaavadata[item] = None
    
    # Copy kaavadata so we are not messing original data up
    kopio = kaavadata.copy()
    
    # Iterate over kaavadata and change it to kaavatietomalli
    for index, row in kaavadata.iterrows():
        
        dictionary = {}
        
        kopio.at[index, 'laji'] = "http://uri.suomi.fi/codelist/rytj/RY_Kaavalaji/code/" + row['kaavalaji']
        kopio.at[index, 'digitaalinenAlkupera'] = "https://koodistot.suomi.fi/code;registryCode=rytj;schemeCode=RY_DigitaalinenAlkupera;codeCode=04"
        try:
            kopio.at[index, 'alueellaSijaitsevaKiinteisto'] = ast.literal_eval(row['kohderekisteriyksikot'])
        except ValueError:
            None
        kopio.at[index, 'nimi'] = row['kuntanimi'] #?
        kopio.at[index, 'kuvaus'] = row['kaavaselite']
        kopio.at[index, 'vireilletuloAika'] = row['hyvaksymispvm']
        
        try:
            dictionary['kaavakartta_sis_maaraykset'] = row['kaavakartta_maar']
        except KeyError:
            None
        try:
            dictionary['kaavakartta'] = row['kaavakartta']
        except KeyError:
            None
        try:
            dictionary['maaraykset'] = row['maaraykset']
        except KeyError:
            None
        try:
            dictionary['selostus'] = row['selostus']
        except KeyError:
            None
        try:
            dictionary['oas'] = row['oas']
        except KeyError:
            None
        try:
            dictionary['muu'] = row['muu']
        except KeyError:
            None
             
        kopio.at[index, 'asianLiite'] = dictionary
        kopio.at[index, 'paikallinenTunnus'] = row[kaavatunnus_col]
    
    # Drop unnecessary columns
    kopio = kopio.drop(col_list, axis=1)
    
    # Pandas to GeoJSON
    geojson = kopio.to_json()
    json_data = json.loads(geojson)
    
    # Add general infromation
    # TÄMÄ TARTTEE VIELÄ MIETTIÄ ERIKSEEN (nyt esim. QGIS tulkitsee name-avaimen tasona, jonka alla kaikki on)
    json_data['name'] = 'VOOKA-etelasavo'
    json_data['crs'] = {"type": "name", "properties": {"name": "urn:ogc:def:crs:EPSG::3067"}}
    
    # Set GeoJSON keys in proper order    
    entity_desired_key_order = ('type', 'name', 'crs', 'features')
    result = ordered(json_data, entity_desired_key_order)
    
    # GeoJSON "pretty print"
    result = json.dumps(result, indent=4)
    
    return(result)
