# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 13:23:18 2022

@author: smassine
"""

def dataToGeoJSON(kaavadata, aineistolahde, ktj_kaavatunnus, kunta_kaavatunnus):
    
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
        else:
            kopio.at[index, "kuvaus"] = "Aluerajaus ja asiakirjat kunnalta"
        
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
            apu_lista = kaavakartta_maar.split(",")
            for item in apu_lista:
                liite_dict = {"asiakirjanTunnus": None,
                              "nimi": None,
                              "laji": None,
                              "lisatietolinkki": None,
                              "metatietokuvaus": None}
                liite_dict['nimi'] = str(item)
                liite_dict['laji'] = ["https://koodistot.suomi.fi/code;registryCode=rytj;schemeCode=RY_AsiakirjanLaji_YKAK;codeCode=03", "https://koodistot.suomi.fi/code;registryCode=rytj;schemeCode=RY_AsiakirjanLaji_YKAK;codeCode=04"]
                liite_lista.append(liite_dict)
        
        # Kaavakartta
        if kaavakartta != None:
            apu_lista = kaavakartta.split(",")
            for item in apu_lista:
                liite_dict = {"asiakirjanTunnus": None,
                              "nimi": None,
                              "laji": None,
                              "lisatietolinkki": None,
                              "metatietokuvaus": None}
                liite_dict['nimi'] = str(item)
                liite_dict['laji'] = "https://koodistot.suomi.fi/code;registryCode=rytj;schemeCode=RY_AsiakirjanLaji_YKAK;codeCode=03"
                liite_lista.append(liite_dict)
        
        # Maaraykset
        if maarays != None:
            apu_lista = maarays.split(",")
            for item in apu_lista:
                liite_dict = {"asiakirjanTunnus": None,
                              "nimi": None,
                              "laji": None,
                              "lisatietolinkki": None,
                              "metatietokuvaus": None}
                liite_dict['nimi'] = str(item)
                liite_dict['laji'] = "https://koodistot.suomi.fi/code;registryCode=rytj;schemeCode=RY_AsiakirjanLaji_YKAK;codeCode=04"
                liite_lista.append(liite_dict)
       
        # Selostukset
        if selostus != None:
            apu_lista = selostus.split(",")
            for item in apu_lista:
                liite_dict = {"asiakirjanTunnus": None,
                              "nimi": None,
                              "laji": None,
                              "lisatietolinkki": None,
                              "metatietokuvaus": None}
                liite_dict['nimi'] = str(item)
                liite_dict['laji'] = "https://koodistot.suomi.fi/code;registryCode=rytj;schemeCode=RY_AsiakirjanLaji_YKAK;codeCode=05"
                liite_lista.append(liite_dict) 
        
        # OAS
        if oas != None:
            apu_lista = oas.split(",")
            for item in apu_lista:
                liite_dict = {"asiakirjanTunnus": None,
                              "nimi": None,
                              "laji": None,
                              "lisatietolinkki": None,
                              "metatietokuvaus": None}
                liite_dict['nimi'] = str(item)
                liite_dict['laji'] = "https://koodistot.suomi.fi/code;registryCode=rytj;schemeCode=RY_AsiakirjanLaji_YKAK;codeCode=13"
                liite_lista.append(liite_dict)
        
        # Muu
        if muu != None:
            apu_lista = muu.split(",")
            for item in apu_lista:
                liite_dict = {"asiakirjanTunnus": None,
                              "nimi": None,
                              "laji": None,
                              "lisatietolinkki": None,
                              "metatietokuvaus": None}
                liite_dict['nimi'] = str(item)
                liite_dict['laji'] = "https://koodistot.suomi.fi/code;registryCode=rytj;schemeCode=RY_AsiakirjanLaji_YKAK;codeCode=99"
                liite_lista.append(liite_dict)
       
        if len(liite_lista) == 0:
            liite_dict = {"asiakirjanTunnus": None,
                          "nimi": None,
                          "laji": None,
                          "lisatietolinkki": None,
                          "metatietokuvaus": None}
            liite_lista.append(liite_dict)
        
        kopio.at[index, 'asianLiite'] = liite_lista
        
        # paikallinenTunnus
        kopio.at[index, 'paikallinenTunnus'] = kunta_kaavatunnus #row[kunta_kaavatunnus]

        # tuottajakohtainenTunnus
        kopio.at[index, 'tuottajakohtainenTunnus'] = row[ktj_kaavatunnus]
        
        ## kaavasuunnitelma
        # kaavalaji
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
        if len(row['kaavaselite']) > 0:
            kaavasuun_dict["kaavanKuvaus"] = row['kaavaselite']
        else:
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
    
    # GeoJSON "pretty print"
    #result = json.dumps(result, indent=4)
    
    return(result)
