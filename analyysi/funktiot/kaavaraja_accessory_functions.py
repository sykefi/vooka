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