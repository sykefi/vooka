# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 10:32:29 2022

@author: smassine
"""

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


def getKuntarajaMaskFromPalstat(palstadata, kuntakoodi, remove_exclaves=False):
    
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
    if str(kuntakoodi) == '681' or str(kuntakoodi) == '507':
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

def clipSavonlinnaByEnonkoski(sln_data, enonkoski_data):
    
    """
    Parameters
    ----------
    sln_data: <gpd.GeoDataFrame>
        Input data (layer to be clipped) as a Geopandas Geodataframe.
    enonkoski_data: <gpd.GeoDataFrame>
        Input data (mask layer) as a Geopandas Geodataframe.
    
    Output
    ------
    <gpd.GeoDataFrame>
        Clipped Geopandas Geodataframe.
    """
    
    import sys
    
    if sln_data.crs['init'] != 'epsg:3067' or enonkoski_data.crs['init'] != 'epsg:3067':
        sys.exit("Your data must have EPSG:3067 (EUREF-TM35FIN) as CRS!")

    clipped = sln_data.difference(enonkoski_data)
    
    return(clipped[0])

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