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


def getKuntarajaMaskFromPalstat(palstadata, kuntakoodi):
    
    """
    A function for clipping kuntaraja mask from MML palstadata.
    
    Parameters
    ----------
    palstadata: <gpd.GeoDataFrame>
        Input data as a Geopandas Geodataframe.
    kuntakoodi: <str> or <int>
        Kuntakoodi for the wanted municipality.
    
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
    
def removeExclaves(wfs_handler_folder, kaavadata, kuntanimi):
    
    """
    A function for removing exclaves that are outside of municipality outlines.
    
    Parameters
    ----------
    wfs_handler_folder: <str>
        Path to folder where get_feature_data.py is stored.
    kaavadata: <gpd.GeoDataFrame>
        Input kaavadata from wanted municipality.
    Kuntanimi <str>
        Name of the municipality.
        
    Output
    ------
    <gpd.GeoDataFrame>
        Kaavadata from wanted municipality. Exclaves excluded.
    """
    
    
    import sys
    sys.path.append(wfs_handler_folder)
    from get_feature_data import getWFSdata
    from shapely.geometry import MultiPolygon, Polygon
    
    mask_data = getWFSdata("https://geo.stat.fi/geoserver/tilastointialueet/wfs", 'tilastointialueet:kunta1000k_2022')
    mask_df = mask_data.loc[mask_data['nimi'] == kuntanimi]
    mask_df_reset = mask_df.reset_index()
    mask = mask_df_reset.at[0, 'geometry']
    
    copy_df = kaavadata.copy()
    
    for index, row in copy_df.iterrows():
        
        if type(row['geometry']) == MultiPolygon:
            
            palat = list(row['geometry'])
            del_list = []
            
            for idx, poly in enumerate(palat):
                if poly.intersects(mask) == False:
                    del_list.append(palat[idx])
            
            new_list = []
            
            for item in palat:
                if item not in del_list:
                    new_list.append(item)
            
            if len(new_list) == 1:
                copy_df.at[index, 'geometry'] = Polygon(new_list[0])
            else:
                copy_df.at[index, 'geometry'] = MultiPolygon(new_list)
            
        elif type(row['geometry']) == Polygon:
            
            if row['geometry'].intersects(mask) == False:
                copy_df.drop(index)
                
        else:
            sys.exit("Geometry has to be either type Polygon or MultiPolygon!")
    
    return(copy_df)


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