# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 13:28:05 2022

@author: smassine
"""

def getDataFromAPI(url, username, password, outfp):
    
    """
    A Function for requesting MML OGC API Features data from "Kiinteistötietojen kyselypalvelu".
    
    Parameters
    ----------
    url: <str>
        A URL to MML feature collection. E.g. Kiinteistörajat: "https://sopimus-paikkatieto.maanmittauslaitos.fi/kiinteisto-avoin/features/v3/collections/KiinteistorajanSijaintitiedot/items"
    username: <str>
        Authentification username for "Kiinteistötietojen kyselypalvelu"
    password: <str>
            Authentification password for "Kiinteistötietojen kyselypalvelu"
    outfp: <str>
        Full output filepath with filename and output format (.pkl). E.g. r"C:\Files\etelasavo_kiinteistorajat.pkl" 
            
    Output
    ------
    <GeoDataFrame>
        Saved pkl-file as a geopandas GeoDataFrame.
    """
    
    import os
    import requests
    import geopandas as gpd
    from shapely.geometry import LineString, Point
    import pickle
    dataframe = gpd.GeoDataFrame()

    # Request URL as JSON with Pohjois-savo bounding box
    url = url + "?f=json&bbox=26.0,61.5,29.1,64.1"
    
    #---------------------------------------------
    #Request URL and list data in dict
    page = 1
    kiinteisto = []
    
    # Connect to API as long as there are pages    
    while True:
            
        try:
            
            if page == 1:
                print('----')
                print("Processing page ", page)
                print('Requesting', url)
                response = requests.get(url , auth = requests.auth.HTTPBasicAuth(username, password))
                data = response.json()
    
                kiinteisto.extend(data['features'])
                page += 1
                    
            else:
                print('----')
                print("Processing page ", page)
                print('Requesting', data['links'][1]['href'])
                response = requests.get(data['links'][1]['href'], auth = requests.auth.HTTPBasicAuth(username, password))
                data = response.json()
    
                kiinteisto.extend(data['features'])
                page += 1
        
        # If last page...
        # Save data and end loop
        except IndexError: # e.g. 1689 pages in KiinteistorajanSijaintitiedot
            print('----')
            print("Page: ", page)
            print("Last page, saving data...")
            dataframe = gpd.GeoDataFrame().from_dict(kiinteisto)
            dataframe.to_pickle(outfp)
            break
    
    return(dataframe)

def normalizeKiinteistorajaSchema(infp, outfp):
    
    """
    A Function for normalizing kiinteistöraja-data requested from MML OGC API Features "Kiinteistötietojen kyselypalvelu".
    
    Parameters
    ----------
    infp: <str>
        Full input filepath with filename and output format (.pkl). E.g. r"C:\Files\etelasavo_kiinteistorajat.pkl"
    outfp: <str>
        Full output filepath with filename and output format (.pkl). E.g. r"C:\Files\etelasavo_kiinteistorajat_norm_schema_TM35.pkl" 
            
    Output
    ------
    <GeoDataFrame>
        Saved pkl-file as a geopandas GeoDataFrame.
    """
    
    import os
    import requests
    import geopandas as gpd
    from shapely.geometry import LineString, Point
    import pickle

    # Open unnormalized kiinteistöraja-data as pkl-file
    with open(infp, "rb") as f:
        kiintrajat = pickle.load(f)
    
    # Set up crs as WGS84
    kiintrajat.crs = {'init' :'epsg:4326'}
    
    # Create new columns for normalization
    kiintrajat['kiinteistorajalaji'] = None
    kiintrajat['lahdeaineisto'] = None
    kiintrajat['interpolointitapa'] = None
    
    #---------------------------------------------
    # Iterate over the dataset and normalize it
    
    i = 1
    
    for index, row in kiintrajat.iterrows():
        
        print("Processing: " + str(i) + "/" + str(len(kiintrajat)))
        
        kiintrajat.at[index, 'geometry'] = LineString(row['geometry']['coordinates'])
        kiintrajat.at[index, 'kiinteistorajalaji'] = row['properties']['kiinteistorajalaji']
        kiintrajat.at[index, 'lahdeaineisto'] = row['properties']['lahdeaineisto']
        kiintrajat.at[index, 'interpolointitapa'] = row['properties']['interpolointitapa']
        
        i = i + 1
    
    # Drop unnecessary columns
    kiintrajat_filtered = kiintrajat.drop(columns=['properties'])
    
    # Project dataset to TM35 crs
    kiintrajat_filtered = kiintrajat_filtered.to_crs(epsg=3067)
    
    # Save outfile to pickle
    # If file already exists, don't copy it again:
    if os.path.isfile(outfp) == True:
        print("")
        print(outfp, "already exists!")
    # If file doesn't already exist, create it
    else:
        print("")
        print("Saving pkl-file...")        
        kiintrajat_filtered.to_pickle(outfp)
    
    return(kiintrajat_filtered)

def normalizeKiinteistotunnusSchema(infp, outfp):
    
    """
    A Function for normalizing kiinteistötunnus-data requested from MML OGC API Features "Kiinteistötietojen kyselypalvelu".
    
    Parameters
    ----------
    infp: <str>
        Full input filepath with filename and output format (.pkl). E.g. r"C:\Files\etelasavo_kiinteistotunnukset.pkl"
    outfp: <str>
        Full output filepath with filename and output format (.pkl). E.g. r"C:\Files\etelasavo_kiinteistotunnukset_norm_schema_TM35.pkl" 
            
    Output
    ------
    <GeoDataFrame>
        Saved pkl-file as a geopandas GeoDataFrame.
    """
    
    import os
    import requests
    import geopandas as gpd
    from shapely.geometry import LineString, Point
    import pickle

    # Open unnormalized kiinteistötunnus-data as pkl-file
    with open(infp, "rb") as f:
        kiinttunnukset = pickle.load(f)
    
    # Set up crs as WGS84
    kiinttunnukset.crs = {'init' :'epsg:4326'}
    
    # Create new columns for normalization
    kiinttunnukset['kiinteistotunnus'] = None
    kiinttunnukset['esitysmuoto'] = None
    
    #---------------------------------------------
    # Iterate over the dataset and normalize it
    
    i = 1
    
    for index, row in kiinttunnukset.iterrows():
        
        print("Processing: " + str(i) + "/" + str(len(kiinttunnukset)))
        
        kiinttunnukset.at[index, 'geometry'] = Point(row['geometry']['coordinates'])
        kiinttunnukset.at[index, 'kiinteistotunnus'] = row['properties']['kiinteistotunnus']
        kiinttunnukset.at[index, 'esitysmuoto'] = row['properties']['kiinteistotunnuksenEsitysmuoto']
        
        i = i + 1
    
    # Drop unnecessary columns
    kiinttunnukset_filtered = kiinttunnukset.drop(columns=['properties'])
    
    # Project dataset to TM35 crs
    kiinttunnukset_filtered = kiinttunnukset_filtered.to_crs(epsg=3067)
    
    # Save outfile to pickle
    # If file already exists, don't copy it again:
    if os.path.isfile(outfp) == True:
        print("")
        print(outfp, "already exists!")
    # If file doesn't already exist, create it
    else:
        print("")
        print("Saving pkl-file...")        
        kiinttunnukset_filtered.to_pickle(outfp)
    
    return(kiinttunnukset_filtered)

def normalizeRajamerkkiSchema(infp, outfp):
    
    """
    A Function for normalizing rajamerkki-data requested from MML OGC API Features "Kiinteistötietojen kyselypalvelu".
    
    Parameters
    ----------
    infp: <str>
        Full input filepath with filename and output format (.pkl). E.g. r"C:\Files\etelasavo_rajamerkit.pkl"
    outfp: <str>
        Full output filepath with filename and output format (.pkl). E.g. r"C:\Files\etelasavo_rajamerkit_norm_schema_TM35.pkl" 
            
    Output
    ------
    <GeoDataFrame>
        Saved pkl-file as a geopandas GeoDataFrame.
    """
    
    import os
    import requests
    import geopandas as gpd
    from shapely.geometry import LineString, Point
    import pickle

    # Open unnormalized rajamerkki-data as pkl-file
    with open(infp, "rb") as f:
        rajamerkit = pickle.load(f)
    
    # Set up crs as WGS84
    rajamerkit.crs = {'init' :'epsg:4326'}
    
    # Create new columns for normalization
    rajamerkit['rajamerkkilaji'] = None
    rajamerkit['numero'] = None
    rajamerkit['tasosijaintitarkkuus'] = None
    rajamerkit['rakenne'] = None
    rajamerkit['lahdeaineisto'] = None
    rajamerkit['suhdeMaanpintaan'] = None
    rajamerkit['olemassaolo'] = None
    
    #---------------------------------------------
    # Iterate over the dataset and normalize it
    
    i = 1
    
    for index, row in rajamerkit.iterrows():
        
        print("Processing: " + str(i) + "/" + str(len(rajamerkit)))
        
        rajamerkit.at[index, 'geometry'] = Point(row['geometry']['coordinates'])
        rajamerkit.at[index, 'rajamerkkilaji'] = row['properties']['rajamerkkilaji']
        rajamerkit.at[index, 'numero'] = row['properties']['numero']
        rajamerkit.at[index, 'tasosijaintitarkkuus'] = row['properties']['tasosijaintitarkkuus']
        rajamerkit.at[index, 'rakenne'] = row['properties']['rakenne']
        rajamerkit.at[index, 'lahdeaineisto'] = row['properties']['lahdeaineisto']
        rajamerkit.at[index, 'suhdeMaanpintaan'] = row['properties']['suhdeMaanpintaan']
        rajamerkit.at[index, 'olemassaolo'] = row['properties']['olemassaolo']
        
        i = i + 1
    
    # Drop unnecessary columns
    rajamerkit_filtered = rajamerkit.drop(columns=['properties'])
    
    # Project dataset to TM35 crs
    rajamerkit_filtered = rajamerkit_filtered.to_crs(epsg=3067)
    
    # Save outfile to pickle
    # If file already exists, don't copy it again:
    if os.path.isfile(outfp) == True:
        print("")
        print(outfp, "already exists!")
    # If file doesn't already exist, create it
    else:
        print("")
        print("Saving pkl-file...")        
        rajamerkit_filtered.to_pickle(outfp)
    
    return(rajamerkit_filtered)
