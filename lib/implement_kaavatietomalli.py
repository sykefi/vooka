# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 13:45:20 2023

@author: VilleHamunen
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
    from shapely.geometry import Polygon, MultiPolygon
    import geojson
    import sys
    import ast
    import geopandas as gpd
    
    # Function to order GeoJSON keys properly
    def ordered(d, desired_key_order):
        return OrderedDict([(key, d[key]) for key in desired_key_order])
    
    # Storing columns to be dropped later
    col_list = kaavadata.columns
    col_list = col_list.drop('geometry')
    
    # Adding new columns based on kaavatietomalli
    # https://tietomallit.ymparisto.fi/kaavatiedot/v1.1/looginenmalli/uml/doc/
    new_columns = [      "planType",
                         "permanentPlanIdentifier",
                         "producerPlanIdentifier",
                         "name",
                         "description",
                         "caseIdentifier",
                         "recordNumbers",
                         "timeOfInitiation",
                         "digitalOrigin",
                         "administrativeAreaIdentifiers",
                         "permanentBindingPlotDivisionIdentifier",
                         "matterAnnexes",
                         "planMatterPhases",
    ]    
    
    for item in new_columns:
        kaavadata[item] = None
    
    # Copy kaavadata so we are not messing original data up
    kopio = kaavadata.copy()  
    
    # Iterate over kaavadata and change it to kaavatietomalli
    for index, row in kaavadata.iterrows():

        
        plantype_definition = {}
        if row['kaavalaji'] == '21':
            plantype_definition = "http://uri.suomi.fi/codelist/rytj/RY_Kaavalaji/code/23"
        else:
            plantype_definition = "http://uri.suomi.fi/codelist/rytj/RY_Kaavalaji/code/" + row['kaavalaji']
        
        
        nimi_definition = {
                                "fin": None,
                                "swe": None,
                                "smn": None,
                                "sms": None,
                                "sme": None,
                                "eng": None,
                                }
        
        
        matterannex_lista = []
        matterAnnex_dict =  {
            "name": {
                "fin": None,
                "swe": None,
                "smn": None,
                "sms": None,
                "sme": None,
                "eng": None,
            },
            "languages": [],
            "documentIdentifier": None,
            "documentDate": None,
            "arrivedDate": None,
            "confirmationDate": None,
            "accessibility": None,
            "documentType": None,
            "documentSpecification": {
                "fin": None,
                "swe": None,
                "smn": None,
                "sms": None,
                "sme": None,
                "eng": None
            },
            "fileKey": None,
            "categoryOfPublicity": None,
            "retentionTime": None,
            "personalDataContent": None,
            "attachmentDocumentKey": None,
            "descriptors": [
                {
                    "descriptorIdentifier": None,
                    "vocabulary": None,
                    "descriptor": None,
                }
            ],
            "typeOfAttachment": None,
            "documentCreatorOperators": [
                {
                    "planOperatorKey": None,
                    "firstName": None,
                    "lastName": None,
                    "title": None,
                    "organizationName": None,
                    "businessId": None,
                }
            ]
        }

        kaava_lista = []
        kaava_dict = {"planKey": None,
                      "planDescription": None,
                      "lifeCycleStatus": "http://uri.suomi.fi/codelist/rytj/kaavaelinkaari/code/13",
                      "legalEffectsOfLocalMasterPlan": None,
                      "scale": None,
                      "planMaps": [
                          {
                              "planMapKey": None,
                              "name": {
                                "fin": None,
                                "swe": None,
                                "smn": None,
                                "sms": None,
                                "sme": None,
                                "eng": None
                                },
                                "fileKey": None,
                                "coordinateSystem": None
                              }
                          ],
                      
                        "geographicalArea": {
                        "srid": "3067"
                        #"geometry": {
                            #"type": None,
                           # "coordinates": None
                        #}
              },
                        
                    
                      "planAnnex": None,
                      "approvalDate": row['hyvaksymispvm'] if row["hyvaksymispvm"] != "NULL" else None,
                      "periodOfValidity":{
                           "begin": row['voimaantulopvm'] if row["voimaantulopvm"] != "NULL" else None,
                           "end": None,
                      },
                      "planCancellationInfo": [
                        {
                        "planCancellationInfoKey": None,
                        "cancelledPlanId": None,
                        "cancelsEntirePlan": None,
                        "cancelledPlanObjectId": [],
                        "cancelledRegulationId": [],
                        "cancelledGuidanceId": [],
                        "cancelledGroupRelations": [
                            {
                                "planRegulationGroupKey": None,
                                "planObjectKey": None
                            }
                        ]
                        }
                    ],
                        "partiallyCancellationPlanObjects": [
                        {
                            "partiallyCancelledPlanObjectId": None,
                            "validityGeometry": {
                                "srid": "3067",
                                "geometry": {}
                            }
                        }
                    ],
                        "planInterruptedInfo": None,
                } 
        
                
        kaavasia_lista = []
        kaavasia_dict = {"planType": None,
                         "permanentPlanIdentifier": None,
                         "producerPlanIdentifier": row['kaavatunnus'] if row["kaavatunnus"] != "NULL" else None,
                             "name": {
                                "fin": None,
                                "swe": None,
                                "smn": None,
                                "sms": None,
                                "sme": None,
                                "eng": None,
                                },
                         "description": {
                                "fin": None,
                                "swe": None,
                                "smn": None,
                                "sms": None,
                                "sme": None,
                                "eng": None,
                                },
                         "caseIdentifier": [],
                         "recordNumbers": [],
                         "timeOfInitiation": None,
                         "digitalOrigin": "http://uri.suomi.fi/codelist/rytj/RY_DigitaalinenAlkupera/code/04",
                         "administrativeAreaIdentifiers": row['kuntakoodi'],
                         "permanentBindingPlotDivisionIdentifier": None,
 
                }
        
                
        kaavasianpaatos_lista = []
        kaavasianpaatos_dict = {
                            "decisionDate": row['voimaantulopvm'] if row["voimaantulopvm"] != "NULL" else None,
                            "dateOfDecision": row['hyvaksymispvm'] if row["hyvaksymispvm"] != "NULL" else None,
                            "typeOfDecisionMaker": "http://uri.suomi.fi/codelist/rytj/PaatoksenTekija/code/02",
                            "decisionDocuments": [
                            {
                                "attachmentDocumentKey": None,
                                "documentIdentifier": None,
                                "name": {
                                    "fin": None,
                                    "swe": None,
                                    "smn": None,
                                    "sms": None,
                                    "sme": None,
                                    "eng": None,
                                },
                                "personalDataContent": None,
                                "categoryOfPublicity": None,
                                "accessibility": None,
                                "retentionTime": None,
                                "confirmationDate": row['vahvistamispvm'] if row["vahvistamispvm"] != "NULL" else None,
                                "languages": [],
                                "fileKey": None,
                                "descriptors": [
                                    {
                                      "descriptorIdentifier": None,
                                      "vocabulary": None,
                                      "descriptor": None,
                                    }
                                ],
                                "documentDate": None,
                                "arrivedDate": None,
                                "typeOfAttachment": None,
                                "documentSpecification": {
                                    "fin": None,
                                    "swe": None,
                                    "smn": None,
                                    "sms": None,
                                    "sme": None,
                                    "eng": None
                                },
                                "documentCreatorOperators": [
                                    {
                                      "planOperatorKey": None,
                                      "firstName": None,
                                      "lastName": None,
                                      "title": None,
                                      "organizationName": None,
                                      "businessId": None,
                }
            ]
        }
    ],                      "decisionText": {
                                    "fin": None,
                                    "swe": None,
                                    "smn": None,
                                    "sms": None,
                                    "sme": None,
                                    "eng": None
                                },
                            "decisionArticle": {
                                    "fin": None,
                                    "swe": None,
                                    "smn": None,
                                    "sms": None,
                                    "sme": None,
                                    "eng": None
                                },
                            "name": "http://uri.suomi.fi/codelist/rytj/kaavpaatnimi/code/11A",
                            "decisionIdentifier": None,
                            "planDecisionKey": None,
                            "statutes": [
                                {
                                "nameOfStatutes": {
                                    "fin": None,
                                    "swe": None,
                                    "smn": None,
                                    "sms": None,
                                    "sme": None,
                                    "eng": None
                                },
                                "numberOfStatuteCollection": None,
                                "yearOfStatuteCollection": None,
                                "chapter": None,
                                "section": None,
                                "subsection": [],
                                "paragraph": [],
                                "subparagraph": [],
                                }
                            ],
                            "plans": kaava_lista
            }
                            
                
                
        kaavasianvaihe_lista = []
        kaavasianvaihe_dict = {
            "planMatterPhaseKey": None,
            "lifeCycleStatus": "http://uri.suomi.fi/codelist/rytj/kaavaelinkaari/code/13",
            "geographicalArea": {
                "srid": None,
                "geometry": None,    
            },
            "planMatterDecisions": kaavasianpaatos_lista
        }
    
        
        toimija_lista = []
        toimija_dict = {
                      "firstName": None,
                      "lastName": None,
                      "title": None,
                      "organisationName": None,
                      "businessId": None,
                      "planOperatorKey": None
        }
        
        #plantype
        kopio.at[index, "planType"] = plantype_definition
        
        
        #producerplanidentifier
        kopio.at[index, "producerPlanIdentifier"] = row['kaavatunnus']
        
        
        # Kaava
        kaava_lista.append(kaava_dict)


        # Kaava-asia
        kaavasia_lista.append(kaavasia_dict)
        
        # Kaava-asian päätös
        kaavasianpaatos_lista.append(kaavasianpaatos_dict)        
        
        
        # Kaava-asian vaihe
        kaavasianvaihe_lista.append(kaavasianvaihe_dict)
        kopio.at[index,"planMatterPhases"] = kaavasianvaihe_lista
        
        #matterannex
        matterannex_lista.append(matterAnnex_dict)
        kopio.at[index,"matterAnnexes"] = matterannex_lista
        
        #nimi
        kopio.at[index, "name"] = nimi_definition
        
        # Toimija
        toimija_lista.append(toimija_dict)      
        
        # kuvaus
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
        if row['kaavatunnus_1'] != "NULL":
            description_value["fin"] += ". KTJ-tunnus: " + row['kaavatunnus_1']

        
        #description
        kopio.at[index, "description"] = description_value
        
        #administrativeareaidentifiers
        kopio.at[index, "administrativeAreaIdentifiers"] = row['kuntakoodi']
    
        #digitalorigin
        kopio.at[index, "digitalOrigin"] = "http://uri.suomi.fi/codelist/rytj/RY_DigitaalinenAlkupera/code/04"
        
        # documents
        liite_lista = []
        
        kaavakarttajamaaraykset = row['kaavakartta_ja_maaraykset']
        kaavakartta = row['kaavakartta']
        maarays = row['maaraykset']
        muu = row['muu']
        
        
        # Kaavakarttajamaaraykset
        if kaavakarttajamaaraykset != "NULL":
            kaavakarttajamaaraykset_str = str(kaavakarttajamaaraykset)
            apu_lista = kaavakarttajamaaraykset_str.split(", ")
            for item in apu_lista:
                liite_dict = {"name": {
                                "fin": None,
                                "swe": None,
                                "smn": None,
                                "sms": None,
                                "sme": None,
                                "eng": None,
                                },
                              "languages": [],
                              "documentIdentifier": None,
                              "documentDate": None,
                              "arrivedDate": None,
                              "confirmationDate": row["vahvistamispvm"] if row["vahvistamispvm"] != "NULL" else None,
                              "accessibility": None,
                              "documentType": None,
                              "documentSpecification":{
                                "fin": None,
                                "swe": None,
                                "smn": None,
                                "sms": None,
                                "sme": None,
                                "eng": None
                              },
                              "fileKey": None,
                              "categoryOfPublicity": None,
                              "retentionTime": None,
                              "personalDataContent": None,
                              "attachmentDocumentKey": None,
                              "descriptors": [
                                  {
                                  "descriptorIdentifier": None,
                                  "vocabulary": None,
                                  "descriptor": None,
                                  }
                              ],
                              "typeOfAttachment": None,
                              "documentCreatorOperators": [
                    {
                      "planOperatorKey": None,
                      "firstName": None,
                      "lastName": None,
                      "title": None,
                      "organizationName": None,
                      "businessId": None,
                    }
                  ]
                }
                liite_dict['name']['fin'] = str(item)
                liite_dict['documentType'] = "http://uri.suomi.fi/codelist/rytj/RY_AsiakirjanLaji_YKAK/code/05"
                liite_dict['categoryOfPublicity'] = "http://uri.suomi.fi/codelist/rytj/julkisuus/code/1" #lähtökohtaisesti kaikki julkisia!
                liite_lista.append(liite_dict)
                
                
        # Kaavakartta
        if kaavakartta != "NULL":
            kaavakartta_str = str(kaavakartta)
            apu_lista = kaavakartta_str.split(", ")
            for item in apu_lista:
                liite_dict = {"name": {
                                "fin": None,
                                "swe": None,
                                "smn": None,
                                "sms": None,
                                "sme": None,
                                "eng": None,
                                },
                              "languages": [],
                              "documentIdentifier": None,
                              "documentDate": None,
                              "arrivedDate": None,
                              "confirmationDate": None,
                              "accessibility": None,
                              "documentType": None,
                              "documentSpecification":{
                                "fin": None,
                                "swe": None,
                                "smn": None,
                                "sms": None,
                                "sme": None,
                                "eng": None
                              },
                              "fileKey": None,
                              "categoryOfPublicity": None,
                              "retentionTime": None,
                              "personalDataContent": None,
                              "attachmentDocumentKey": None,
                              "descriptors": [
                                  {
                                  "descriptorIdentifier": None,
                                  "vocabulary": None,
                                  "descriptor": None,
                                  }
                              ],
                              "typeOfAttachment": None,
                              "documentCreatorOperators": [
                    {
                      "planOperatorKey": None,
                      "firstName": None,
                      "lastName": None,
                      "title": None,
                      "organizationName": None,
                      "businessId": None,
                    }
                  ]
                }
                liite_dict['name']['fin'] = str(item)
                liite_dict['documentType'] = "http://uri.suomi.fi/codelist/rytj/RY_AsiakirjanLaji_YKAK/code/03"
                liite_dict['categoryOfPublicity'] = "http://uri.suomi.fi/codelist/rytj/julkisuus/code/1" #lähtökohtaisesti kaikki julkisia!
                liite_lista.append(liite_dict)
        
        
        # Maaraykset
        if maarays != "NULL":
            maarays_str = str(maarays)
            apu_lista = maarays_str.split(", ")
            for item in apu_lista:
                liite_dict = {"name": {
                                "fin": None,
                                "swe": None,
                                "smn": None,
                                "sms": None,
                                "sme": None,
                                "eng": None,
                                },
                              "languages": [],
                              "documentIdentifier": None,
                              "documentDate": None,
                              "arrivedDate": None,
                              "confirmationDate": None,
                              "accessibility": None,
                              "documentType": None,
                              "documentSpecification":{
                                "fin": None,
                                "swe": None,
                                "smn": None,
                                "sms": None,
                                "sme": None,
                                "eng": None
                              },
                              "fileKey": None,
                              "categoryOfPublicity": None,
                              "retentionTime": None,
                              "personalDataContent": None,
                              "attachmentDocumentKey": None,
                              "descriptors": [
                                  {
                                  "descriptorIdentifier": None,
                                  "vocabulary": None,
                                  "descriptor": None,
                                  }
                              ],
                              "typeOfAttachment": None,
                              "documentCreatorOperators": [
                    {
                      "planOperatorKey": None,
                      "firstName": None,
                      "lastName": None,
                      "title": None,
                      "organizationName": None,
                      "businessId": None,
                    }
                  ]
                }
                liite_dict['name']['fin'] = str(item)
                liite_dict['documentType'] = "http://uri.suomi.fi/codelist/rytj/RY_AsiakirjanLaji_YKAK/code/04"
                liite_dict['categoryOfPublicity'] = "http://uri.suomi.fi/codelist/rytj/julkisuus/code/1" #lähtökohtaisesti kaikki julkisia!
                liite_lista.append(liite_dict)
       
        
        # Muu
        if muu != "NULL":
            muu_str = str(muu)
            apu_lista = muu_str.split(", ")
            for item in apu_lista:
                liite_dict = {"name": {
                                "fin": None,
                                "swe": None,
                                "smn": None,
                                "sms": None,
                                "sme": None,
                                "eng": None,
                                },
                              "languages": [],
                              "documentIdentifier": None,
                              "documentDate": None,
                              "arrivedDate": None,
                              "confirmationDate": None,
                              "accessibility": None,
                              "documentType": None,
                              "documentSpecification":{
                                "fin": None,
                                "swe": None,
                                "smn": None,
                                "sms": None,
                                "sme": None,
                                "eng": None
                              },
                              "fileKey": None,
                              "categoryOfPublicity": None,
                              "retentionTime": None,
                              "personalDataContent": None,
                              "attachmentDocumentKey": None,
                              "descriptors": [
                                  {
                                  "descriptorIdentifier": None,
                                  "vocabulary": None,
                                  "descriptor": None,
                                  }
                              ],
                              "typeOfAttachment": None,
                              "documentCreatorOperators": [
                    {
                      "planOperatorKey": None,
                      "firstName": None,
                      "lastName": None,
                      "title": None,
                      "organizationName": None,
                      "businessId": None,
                    }
                  ]
                }
                liite_dict['name']['fin'] = str(item)
                liite_dict['documentType'] = "http://uri.suomi.fi/codelist/rytj/RY_AsiakirjanLaji_YKAK/code/99"
                liite_dict['categoryOfPublicity'] = "http://uri.suomi.fi/codelist/rytj/julkisuus/code/1" #lähtökohtaisesti kaikki julkisia!
                liite_lista.append(liite_dict)
       
       
        if len(liite_lista) == 0:
                liite_dict = {"name": {
                                "fin": None,
                                "swe": None,
                                "smn": None,
                                "sms": None,
                                "sme": None,
                                "eng": None,
                                },
                              "languages": [],
                              "documentIdentifier": None,
                              "documentDate": None,
                              "arrivedDate": None,
                              "confirmationDate": None,
                              "accessibility": None,
                              "documentType": None,
                              "documentSpecification":{
                                "fin": None,
                                "swe": None,
                                "smn": None,
                                "sms": None,
                                "sme": None,
                                "eng": None
                              },
                              "fileKey": None,
                              "categoryOfPublicity": None,
                              "retentionTime": None,
                              "personalDataContent": None,
                              "attachmentDocumentKey": None,
                              "descriptors": [
                                  {
                                  "descriptorIdentifier": None,
                                  "vocabulary": None,
                                  "descriptor": None,
                                  }
                              ],
                              "typeOfAttachment": None,
                              "documentCreatorOperators": [
                    {
                      "planOperatorKey": None,
                      "firstName": None,
                      "lastName": None,
                      "title": None,
                      "organizationName": None,
                      "businessId": None,
                    }
                  ]
                }
                liite_lista.append(liite_dict)
        
        kaava_dict["planAnnex"] = liite_lista

        
        # kaavalaji
        if row['kaavalaji'] == '21':
            kaavasia_dict["planType"] = "http://uri.suomi.fi/codelist/rytj/RY_Kaavalaji/code/23"
        else:
            kaavasia_dict["planType"] = "http://uri.suomi.fi/codelist/rytj/RY_Kaavalaji/code/" + row['kaavalaji']
        
        # Yleiskaavat oikeusvaikutus
        # First check if kaavalaji is not 21 or 23, give it None
        if row['kaavalaji'] not in ['21', '23']:
            kaava_dict["legalEffectsOfLocalMasterPlan"] = None
        else:
            if row['kaavalaji'] != '25':
                kaava_dict["legalEffectsOfLocalMasterPlan"] = "http://uri.suomi.fi/codelist/rytj/RY_OikeusvaikutteisuudenLaji/code/01"
            else:
                kaava_dict["legalEffectsOfLocalMasterPlan"] = "http://uri.suomi.fi/codelist/rytj/RY_OikeusvaikutteisuudenLaji/code/02"
    
    
        kaava_dict["geographicalArea"] = geojson.Feature(geometry=row['geometry'])
        kaava_dict["geographicalArea"]["srid"] = "3067"

    #kaava_dict["geographicalArea"]["geometry"] = mapping(row['geometry'])
        
        
    # Drop unnecessary columns
    kopio = kopio.drop(col_list, axis=1)
    
    # Pandas to GeoJSON
    geojson = kopio.to_json()
    json_data = json.loads(geojson)
    
    # Extract "features" part from GeoJSON
    features_only = json_data.get("features", [])
    
    # Extract only "properties" part from each feature
    properties_only = [feature.get("properties", {}) for feature in features_only]

    return(properties_only)

