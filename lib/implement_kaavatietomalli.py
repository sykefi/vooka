# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 13:23:18 2022
Modified on Tue Feb 20 15:32:20 2024

"""

def dataToJSON(kaavadata, aineistolahde, ktj_kaavatunnus, kunta_kaavatunnus):
    
    """
    A function for creating a JSON file (collections.OrderedDict) from Geopandas GeoDataFrame.
    
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
    from shapely.geometry import Polygon, MultiPolygon
    from shapely.geometry import mapping
    from shapely.ops import transform
    import sys
    import geopandas as gpd
    import uuid
    
    # Function to remove Z coordinate from any geometry
    def remove_z(geometry):
        if geometry.has_z:
            # Create a 2D geometry without the Z dimension
            return transform(lambda x, y, z=None: (x, y), geometry)
        else:
            return geometry

    # Function to convert MultiPolygon to Polygon if it contains only one Polygon, and remove Z values
    def convert_multipolygon_and_remove_z(geometry):
        # Remove Z values first
        geometry_no_z = remove_z(geometry)
        
        # Then check if it's a MultiPolygon with only one Polygon
        if isinstance(geometry_no_z, MultiPolygon) and len(geometry_no_z.geoms) == 1:
            # Return the first Polygon without Z values
            return geometry_no_z.geoms[0]
        else:
            return geometry_no_z
    
    # Function to recursively search and update dictionary keys
    def update_guids(obj):
        if isinstance(obj, dict):
            for key, value in obj.items():
                if isinstance(value, (dict, list)):
                    update_guids(value)
                # Define the condition for assigning a new GUID (= if key ends with 'Key' and is not 'fileKey')
                if key.endswith('Key') and key != 'fileKey':
                    obj[key] = str(uuid.uuid4())
        elif isinstance(obj, list):
            for item in obj:
                update_guids(item)
    
    # Function to order JSON keys properly
    def ordered(d, desired_key_order):
        return OrderedDict([(key, d[key]) for key in desired_key_order])
    
    # Validate geometries and remove unnecessary z values
    kaavadata['geometry'] = kaavadata['geometry'].apply(convert_multipolygon_and_remove_z)
    
    # Storing columns to be dropped later
    col_list = kaavadata.columns
    col_list = col_list.drop('geometry')
    
    # Adding new columns based on kaavatietomalli
    # https://tietomallit.ymparisto.fi/kaavatiedot/v1.1/looginenmalli/uml/doc/
    new_columns = [     "permanentPlanIdentifier",
                        "planType",
                        "name",
                        "timeOfInitiation",
                        "description",
                        "producerPlanIdentifier",
                        "caseIdentifiers",
                        "bindingPlotDivisionIdentifier",
                        "recordNumbers",
                        "administrativeAreaIdentifiers",
                        "digitalOrigin",
                        "planMatterPhases",
                  ]    
    
    for item in new_columns:
        kaavadata[item] = None
    
    # Copy kaavadata so we are not messing original data up
    kopio = kaavadata.copy()  
    
    # Iterate over kaavadata and change it to kaavatietomalli
    for index, row in kaavadata.iterrows():
        
        # planMatter
        kopio.at[index, "planType"] = "http://uri.suomi.fi/codelist/rytj/RY_Kaavalaji/code/" + row['kaavalaji']
        
        name_value = {
                        "fin": None,
                        "swe": None,
                        "smn": None,
                        "sms": None,
                        "sme": None,
                        "eng": None,
                     }
        
        if row['kaavaselite'] in ["NULL", None]:
            if row['kaavalaji'] == '21':
                name_value["fin"] = "Yleiskaava " + (row["kaavatunnus"] if row["kaavatunnus"] not in ["NULL", None] else row["kaavatunnus_1"])
            elif row['kaavalaji'] == '22':
                name_value["fin"] = "Vaiheyleiskaava " + (row["kaavatunnus"] if row["kaavatunnus"] not in ["NULL", None] else row["kaavatunnus_1"])
            elif row['kaavalaji'] == '23':
                name_value["fin"] = "Osayleiskaava " + (row["kaavatunnus"] if row["kaavatunnus"] not in ["NULL", None] else row["kaavatunnus_1"])
            elif row['kaavalaji'] == '24':
                name_value["fin"] = "Kuntien yhteinen yleiskaava " + (row["kaavatunnus"] if row["kaavatunnus"] not in ["NULL", None] else row["kaavatunnus_1"])
            elif row['kaavalaji'] == '25':
                name_value["fin"] = "Maanalainen yleiskaava " + (row["kaavatunnus"] if row["kaavatunnus"] not in ["NULL", None] else row["kaavatunnus_1"])
            elif row['kaavalaji'] == '31':
                name_value["fin"] = "Asemakaava " + (row["kaavatunnus"] if row["kaavatunnus"] not in ["NULL", None] else row["kaavatunnus_1"])
            elif row['kaavalaji'] == '32':
                name_value["fin"] = "Vaiheasemakaava " + (row["kaavatunnus"] if row["kaavatunnus"] not in ["NULL", None] else row["kaavatunnus_1"])
            elif row['kaavalaji'] == '33':
                name_value["fin"] = "Ranta-asemakaava " + (row["kaavatunnus"] if row["kaavatunnus"] not in ["NULL", None] else row["kaavatunnus_1"])
            elif row['kaavalaji'] == '34':
                name_value["fin"] = "Vaiheranta-asemakaava " + (row["kaavatunnus"] if row["kaavatunnus"] not in ["NULL", None] else row["kaavatunnus_1"])
            elif row['kaavalaji'] == '35':
                name_value["fin"] = "Maanalaisten tilojen asemakaava " + (row["kaavatunnus"] if row["kaavatunnus"] not in ["NULL", None] else row["kaavatunnus_1"])
            elif row['kaavalaji'] == '39':
                name_value["fin"] = "Asemakaava (ohjeellinen tonttijako) " + (row["kaavatunnus"] if row["kaavatunnus"] not in ["NULL", None] else row["kaavatunnus_1"])
            else:
                sys.exit("You have invalid 'kaavalaji' in your data!")
        else:
            name_value["fin"] = row['kaavaselite']
        
        kopio.at[index, "name"] = name_value
        
        kopio.at[index, "timeOfInitiation"] = "1900-01-01"
        kopio.at[index, "producerPlanIdentifier"] = row['kaavatunnus'] if row["kaavatunnus"] not in ["NULL", None] else None
        kopio.at[index, "caseIdentifiers"] = []
        kopio.at[index, "recordNumbers"] = []
        kopio.at[index, "administrativeAreaIdentifiers"] = [row['kuntakoodi']]
        kopio.at[index, "digitalOrigin"] = "http://uri.suomi.fi/codelist/rytj/RY_DigitaalinenAlkupera/code/04"
        
        # plan
        kaava_lista = []
        kaava_dict = {
                        "planKey": None,
                        "lifeCycleStatus": "http://uri.suomi.fi/codelist/rytj/kaavaelinkaari/code/13",
                        "legalEffectsOfLocalMasterPlan": "http://uri.suomi.fi/codelist/rytj/oikeusvaik_YK/code/1" if row['kaavalaji'] in ["21", "22", "23", "24", "25"] else None,
                        "scale": None,
                        "geographicalArea": {
                            "srid": "3067",
                            "geometry": {
                                "type": None,
                                "coordinates": None
                            }
                        },
                        "planDescription": None,
                        "periodOfValidity":{
                             "begin": row['voimaantulopvm'] if row["voimaantulopvm"] not in ["NULL", None] else "1900-01-01",
                             "end": None,
                        },
                        "approvalDate": row['hyvaksymispvm'] if row["hyvaksymispvm"] not in ["NULL", None] else None
                     } 
        
        # planDecisions
        kaavasianpaatos_lista = []
        kaavasianpaatos_dict = {
                                    "planDecisionKey": None,
                                    "name": "http://uri.suomi.fi/codelist/rytj/kaavpaatnimi/code/11A",
                                    "decisionDate": row['voimaantulopvm'] if row["voimaantulopvm"] not in ["NULL", None] else "1900-01-01",
                                    "dateOfDecision": row['hyvaksymispvm'] if row["hyvaksymispvm"] not in ["NULL", None] else "1900-01-01",
                                    "dateOfValidity": "1900-01-01",
                                    "decisionDocuments": [], 
                                    "decisionArticle": None,
                                    "decisionText": None,
                                    "typeOfDecisionMaker": "http://uri.suomi.fi/codelist/rytj/PaatoksenTekija/code/02",
                                    "decisionIdentifier": None,
                                    "plans": kaava_lista
            }
                            
                
        # planMatterPhases
        kaavasianvaihe_lista = []
        kaavasianvaihe_dict = {
            "planMatterPhaseKey": None,
            "lifeCycleStatus": "http://uri.suomi.fi/codelist/rytj/kaavaelinkaari/code/13",
            "geographicalArea": {
                "srid": None,
                "geometry": {}
              },
            "planDecisions": kaavasianpaatos_lista
        }
        
        # plan
        kaava_lista.append(kaava_dict)
        
        # planDecisions
        kaavasianpaatos_lista.append(kaavasianpaatos_dict)        
        
        # planMatterPhases
        kaavasianvaihe_lista.append(kaavasianvaihe_dict)
        kopio.at[index,"planMatterPhases"] = kaavasianvaihe_lista
        
        # description
        description_value = {
            "fin": None,
            "swe": None,
            "smn": None,
            "sms": None,
            "sme": None,
            "eng": None
            }
        if aineistolahde == "KTJ":
            description_value["fin"] = "Aluerajaus KTJ-aineistosta, asiakirjat kunnalta"
        elif aineistolahde == "kunta":
            description_value["fin"] = "Aluerajaus ja asiakirjat kunnalta"
        else:
            sys.exit("Your 'aineistolahde' parameter must be either 'KTJ' or 'kunta'!")
        
       # Check if 'Kuvaus' exists in the row and concatenate it with existing description
        if 'Kuvaus' in row:
            description_value["fin"] += ". " + row['Kuvaus']
        
        # Check if 'Kaavatunnus1' exists in the row and concatenate it with existing description
        if row['kaavatunnus_1'] not in ["NULL", None]:
            description_value["fin"] += " KTJ-tunnus: " + row['kaavatunnus_1']

        kopio.at[index, "description"] = description_value
        
        # documents
        liite_lista = []
        
        kaavakarttajamaaraykset = row['kaavakartta_ja_maaraykset']
        kaavakartta = row['kaavakartta']
        maarays = row['maaraykset']
        muu = row['muu']
        
        
        # Kaavakarttajamaaraykset
        if kaavakarttajamaaraykset not in ["NULL", None]:
            kaavakarttajamaaraykset_str = str(kaavakarttajamaaraykset)
            apu_lista = kaavakarttajamaaraykset_str.split(", ")
            for item in apu_lista:
                liite_dict = {
                    "attachmentDocumentKey": None,
                    "documentIdentifier": "Ei tiedossa",
                    "name": {
                        "fin": "Kaavakartta ja kaavamääräykset, " + str(item),
                        "swe": None,
                        "smn": None,
                        "sms": None,
                        "sme": None,
                        "eng": None,
                    },
                    "personalDataContent": "http://uri.suomi.fi/codelist/rytj/henkilotietosisalto/code/1",
                    "categoryOfPublicity": "http://uri.suomi.fi/codelist/rytj/julkisuus/code/1",
                    "accessibility": True,
                    "retentionTime": "http://uri.suomi.fi/codelist/rytj/sailytysaika/code/01",
                    "confirmationDate": row['vahvistamispvm'] if row["vahvistamispvm"] not in ["NULL", None] else None,
                    "languages": ["http://uri.suomi.fi/codelist/rytj/ryhtikielet/code/fi"],
                    "fileKey": None,
                    "documentDate": "1900-01-01",
                    "arrivedDate": None,
                    "typeOfAttachment": "http://uri.suomi.fi/codelist/rytj/RY_AsiakirjanLaji_YKAK/code/05",
                    "documentSpecification": None
                }
                liite_lista.append(liite_dict)
                
                
        # Kaavakartta
        if kaavakartta not in ["NULL", None]:
            kaavakartta_str = str(kaavakartta)
            apu_lista = kaavakartta_str.split(", ")
            for item in apu_lista:
                liite_dict = {
                    "attachmentDocumentKey": None,
                    "documentIdentifier": "Ei tiedossa",
                    "name": {
                        "fin": "Kaavakartta, " + str(item),
                        "swe": None,
                        "smn": None,
                        "sms": None,
                        "sme": None,
                        "eng": None,
                    },
                    "personalDataContent": "http://uri.suomi.fi/codelist/rytj/henkilotietosisalto/code/1",
                    "categoryOfPublicity": "http://uri.suomi.fi/codelist/rytj/julkisuus/code/1",
                    "accessibility": True,
                    "retentionTime": "http://uri.suomi.fi/codelist/rytj/sailytysaika/code/01",
                    "confirmationDate": row['vahvistamispvm'] if row["vahvistamispvm"] not in ["NULL", None] else None,
                    "languages": ["http://uri.suomi.fi/codelist/rytj/ryhtikielet/code/fi"],
                    "fileKey": None,
                    "documentDate": "1900-01-01",
                    "arrivedDate": None,
                    "typeOfAttachment": "http://uri.suomi.fi/codelist/rytj/RY_AsiakirjanLaji_YKAK/code/03",
                    "documentSpecification": None
                }
                liite_lista.append(liite_dict)
        
        
        # Maaraykset
        if maarays not in ["NULL", None]:
            maarays_str = str(maarays)
            apu_lista = maarays_str.split(", ")
            for item in apu_lista:
                liite_dict = {
                    "attachmentDocumentKey": None,
                    "documentIdentifier": "Ei tiedossa",
                    "name": {
                        "fin": "Kaavamääräykset, " + str(item),
                        "swe": None,
                        "smn": None,
                        "sms": None,
                        "sme": None,
                        "eng": None,
                    },
                    "personalDataContent": "http://uri.suomi.fi/codelist/rytj/henkilotietosisalto/code/1",
                    "categoryOfPublicity": "http://uri.suomi.fi/codelist/rytj/julkisuus/code/1",
                    "accessibility": True,
                    "retentionTime": "http://uri.suomi.fi/codelist/rytj/sailytysaika/code/01",
                    "confirmationDate": row['vahvistamispvm'] if row["vahvistamispvm"] not in ["NULL", None] else None,
                    "languages": ["http://uri.suomi.fi/codelist/rytj/ryhtikielet/code/fi"],
                    "fileKey": None,
                    "documentDate": "1900-01-01",
                    "arrivedDate": None,
                    "typeOfAttachment": "http://uri.suomi.fi/codelist/rytj/RY_AsiakirjanLaji_YKAK/code/04",
                    "documentSpecification": None
                }
                liite_lista.append(liite_dict)
       
        
        # Muu
        if muu not in ["NULL", None]:
            muu_str = str(muu)
            apu_lista = muu_str.split(", ")
            for item in apu_lista:
                liite_dict = {
                    "attachmentDocumentKey": None,
                    "documentIdentifier": "Ei tiedossa",
                    "name": {
                        "fin": "Muu asiakirja, " + str(item),
                        "swe": None,
                        "smn": None,
                        "sms": None,
                        "sme": None,
                        "eng": None,
                    },
                    "personalDataContent": "http://uri.suomi.fi/codelist/rytj/henkilotietosisalto/code/1",
                    "categoryOfPublicity": "http://uri.suomi.fi/codelist/rytj/julkisuus/code/1",
                    "accessibility": True,
                    "retentionTime": "http://uri.suomi.fi/codelist/rytj/sailytysaika/code/01",
                    "confirmationDate": row['vahvistamispvm'] if row["vahvistamispvm"] not in ["NULL", None] else None,
                    "languages": ["http://uri.suomi.fi/codelist/rytj/ryhtikielet/code/fi"],
                    "fileKey": None,
                    "documentDate": "1900-01-01",
                    "arrivedDate": None,
                    "typeOfAttachment": "http://uri.suomi.fi/codelist/rytj/RY_AsiakirjanLaji_YKAK/code/99",
                    "documentSpecification": None
                }
                liite_lista.append(liite_dict)
        
        kaavasianpaatos_dict["decisionDocuments"] = liite_lista
        
        # Convert Shapely geometry into GeoJSON
        row_geometry_json = mapping(row['geometry'])
        
        kaava_dict["geographicalArea"]["srid"] = "3067"
        kaava_dict["geographicalArea"]["geometry"]["type"] = row_geometry_json['type']
        kaava_dict["geographicalArea"]["geometry"]["coordinates"] = row_geometry_json['coordinates']
        
        
    # Drop unnecessary columns
    kopio = kopio.drop(col_list, axis=1)
    
    # Pandas to JSON
    geo_json = kopio.to_json()
    json_data = json.loads(geo_json)
    
    # Extract "features" part from JSON
    features_only = json_data.get("features", [])
    
    # Extract only "properties" part from each feature
    properties_only = [feature.get("properties", {}) for feature in features_only]
    
    # Update GUIDs in the loaded data
    update_guids(properties_only)
    
    # Sort objects accordingly
    keyorder = ('permanentPlanIdentifier', 'planType', 'name', 'timeOfInitiation', 'description', 'producerPlanIdentifier', 'caseIdentifiers', 'bindingPlotDivisionIdentifier', 'recordNumbers', 'administrativeAreaIdentifiers', 'digitalOrigin', 'planMatterPhases')
    sorted_list = []
    
    for item in properties_only:
        new_item = ordered(item, keyorder)
        sorted_list.append(new_item)
    
    return(sorted_list)
