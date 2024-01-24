# -*- coding: utf-8 -*-
"""
Accessory functions for VOOKA ETL usage.
"""

import os
import requests
import pandas as pd


def readPickleData(inputfp):
    
    """
    Parameters
    ----------
    inputfp: <str> <gpd.GeoDataFrame>
        Full input filepath with filename and format (.pkl). E.g. r"C:\Files\etelasavo_palstat.pkl"
        
    Output
    ------
    <gpd.GeoDataFrame>
        Data as Geopandas Geodataframe.
    """
    
    import pickle
    
    with open(inputfp, "rb") as f:
        palstat = pickle.load(f)
    
    return(palstat)


def getKuntarajaMaskFromPalstat(palstadata, kuntakoodi, fill_holes=True, remove_exclaves=False):
    
    """
    A function for clipping kuntaraja mask from MML palstadata.
    
    Mandatory parameters
    --------------------
    palstadata: <gpd.GeoDataFrame>
        Input data as a Geopandas Geodataframe.
    kuntakoodi: <str> or <int>
        Kuntakoodi for the wanted municipality.
        
    Optional parameters
    -------------------
    fill_holes: <boolean>
        True/False (True default)
        Fills Polygon holes in kuntarajamask when True.

    remove_exclaves <boolean>
        True/False (False default).
        Removes small exclaves outside the municipality if True.
    
    Output
    ------
    <shapely.geometry.polygon.Polygon>
        Kuntaraja mask as a Shapely Polygon.
    """
    
    import geopandas as gpd
    from shapely.ops import unary_union
    from shapely.geometry import MultiPolygon, Polygon
    import sys

    if palstadata.crs['init'] != 'epsg:3067':
        sys.exit("Your data must have EPSG:3067 (EUREF-TM35FIN) as CRS!")
    
    master_df = gpd.GeoDataFrame(columns=["geometry"], geometry="geometry", crs={'init': 'epsg:3067'})
    
    i = 1
    
    for index, row in palstadata.iterrows():
        
        print("Processing kuntarajamaski: " + str(i) + "/" + str(len(palstadata)))
        
        if str(kuntakoodi) == '046':
            if row['properties']['kiinteistotunnuksenEsitysmuoto'][0:3] == '46-':
                row_schema = {'geometry': row.geometry}
                master_df = master_df.append(row_schema, ignore_index=True)
        elif str(kuntakoodi) == '097':
            if row['properties']['kiinteistotunnuksenEsitysmuoto'][0:3] == '97-':
                row_schema = {'geometry': row.geometry}
                master_df = master_df.append(row_schema, ignore_index=True)
        else:
            if row['properties']['kiinteistotunnuksenEsitysmuoto'][0:3] == str(kuntakoodi):
                row_schema = {'geometry': row.geometry}
                master_df = master_df.append(row_schema, ignore_index=True)
            
        i = i + 1
        
    geom_list = list(master_df['geometry'])
    mask = unary_union(geom_list)
    
    if remove_exclaves == True:
        poly_list = list(mask)
        max_value = 0
        max_index = None
        
        for idx, poly in enumerate(poly_list):
            if poly.area > max_value:
                max_value = poly.area
                max_index = idx
        
        mother_poly = Polygon(poly_list[max_index].exterior)
        del_list = []
        
        for idxx, item in enumerate(poly_list):
            if item.within(mother_poly) == False:
                del_list.append(poly_list[idxx])
        
        new_list = []
            
        for item in poly_list:
            if item not in del_list:
                new_list.append(item)
        
        if len(new_list) == 1:
            mask = Polygon(new_list[0])
        else:
            mask = MultiPolygon(new_list)
        
    # FIll holes
    if fill_holes == False:
        return(mask)
    else:
        if type(mask) == Polygon:
            no_holes_mask = Polygon(Polygon(mask.exterior))
        elif type(mask) == MultiPolygon:
            no_holes_mask = MultiPolygon(Polygon(poly.exterior) for poly in mask)
        else:
            sys.exit("Your mask should be either type Polygon or MultiPolygon! Check your code/data!")
    
        return(no_holes_mask)

def saveGPKG(input_data, outputfp, layer_name):
    
    """
    Parameters
    ----------
    inputdata: <str> <gpd.GeoDataFrame>
        Input data as a Geopandas Geodataframe.
    outputfp: <str>
        Full output filepath with filename and format (.gpkg). E.g. r"C:\Files\kuntamaskit.gpkg"
    layer_name: <str>
        Layer in Geopackage. E.g. "Juva"
    """
    
    input_data.to_file(outputfp, layer=layer_name, driver="GPKG")
    
    return()

def setupMasterGDF(data, geom_column):
    
    """
    Parameters
    ----------
    data: <gpd.GeoDataFrame>
        Input data to set up master dataframe schema. Schema will be created based on data's coordinate reference system and columns.
    geom_column: <str>
        Data's geometry column name as a string value.
    
    Output
    ------
    <gpd.GeoDataFrame>
        An empty Geopandas GeoDataFrame.
    """
    
    import geopandas as gpd
    
    master_df = gpd.GeoDataFrame(columns=list(data.columns), geometry=geom_column, crs=data.crs)
    
    return(master_df)

def appendDataToMaster(master_data, append_data):
    
    """
    Parameters
    ----------
    master_data: <gpd.GeoDataFrame> or <pp.Dataframe>
        Master dataframe. Can be an empty dataframe or including value rows.
    append_data: <str>
        Data to be appended to master.
    
    Output
    ------
    <gpd.GeoDataFrame> or <pd.Dataframe>
        Master dataframe with appended value rows.
    """
    
    import sys
    import pandas as pd
    
    if master_data.crs['init'] != append_data.crs['init']:
        sys.exit("Your data must have the same coordinate reference system as master dataframe!")
    if list(master_data.columns) != list(append_data.columns):
        sys.exit("Data to be appended must have same schema as master dataframe!")
    master = pd.concat([master_data, append_data], ignore_index=True)
    
    return(master)

def stringColumnToDate(input_df, date_column):
    
    """
    A function for changing string date values to date values in a Pandas Dataframe.
    
    Parameters
    --------------------
    input_df: <pd.Dataframe> or <gpd.GeoDataFrame>
        Input data as a Pandas Dataframe or Geopandas Geodataframe.
    date_column: <str>
        Name of the date column in which the string date values to be transformed are.
    
    Output
    ------
    <pd.Dataframe> or <gpd.GeoDataFrame>
        Input dataframe with altered date values in a column.
    """
    
    import sys
    from dateutil import parser
    
    def contains_number(string):
        return any(char.isdigit() for char in string)
    
    input_df['new_date_column'] = None
    
    for index, row in input_df.iterrows():
        
        try:
        
            date_str = row[date_column]
            
            if date_str != None:
                # 178 yksi erilliskäsittely
                if date_str[0:5] == 'xx.xx' and row['kaavaselite'] == 'Kirkonseutu Jukajärvi rakennuskaavan muutos':
                    date_str = '10.2.1983'
                # 213 kirjausvirhe
                elif date_str == '20042208' and row['kaavaselite'] == 'Reinikkalan ranta-asemakaavan muutos 2004':
                    date_str = '20041108'
                # 588 pari erilliskäsittelyä
                elif date_str[0:8].lower() == 'e-sympk.' and row['kuntakoodi'] == '588':
                    date_str = date_str[0:-14]
                elif date_str[0:20].lower() == 'osittain vahv. ymp.k' and row['kuntakoodi'] == '588':
                    date_str = date_str[-9:]
                # 097 yksi erilliskäsittely
                elif date_str == '1977, 1988' and row['kaavaselite'] == 'ETUNIEMEN RANTAKAAVAN MUUTOS':
                    date_str = '1.1.' + date_str[-4:]
                # Vain vuosi ilmoitettu
                elif len(date_str) == 4 and contains_number(date_str) == True:
                    date_str = '1.1.' + date_str
                else:
                    None
            
            if str(date_str) == '0':
                date_str = None
                    
            if contains_number(date_str) == True:
                
                try:
                    res = parser.parse(date_str, fuzzy=True)
                    res_date = res.date()
                    input_df.at[index, 'new_date_column'] = str(res_date)
                        
                except ValueError:
                    date_str = date_str[0:-4]
                    res = parser.parse(date_str, fuzzy=True)
                    res_date = res.date()
                    input_df.at[index, 'new_date_column'] = str(res_date)
                        
            else:
                res_date = None
                input_df.at[index, 'new_date_column'] = res_date
            
        except TypeError:
            if type(date_str) == type(None):
                res_date = None
                input_df.at[index, 'new_date_column'] = res_date
            else:
                sys.exit("TypeError occured that is not NoneType. Check your data on index " + str(index) + ".")
        
        #if date_str is not None:
            #print("Old string date: " + str(row[date_column]))
            #print("New date as datetime.date: " + str(res_date))
    
    input_df = input_df.drop([date_column], axis=1)
    input_df = input_df.rename(columns={'new_date_column': date_column})

    return(input_df)



def download_file(url, save_path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=128):
                file.write(chunk)
        print(f"Ladattu: {save_path}")
        print("")
    else:
        print(f"LATAUS EPÄONNISTUI: {url}")
        print("")


def create_folder(folder_path):
    try:
        # Try to create the folder
        os.makedirs(folder_path)
    except FileExistsError:
        # If the folder already exists, catch the exception and inform the user
        print(f"'{folder_path}' on jo olemassa.")
        print("Poista kansio tai valitse uusi kansionimi.")
        return False
        