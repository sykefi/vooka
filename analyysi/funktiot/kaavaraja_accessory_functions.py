# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 10:32:29 2022

@author: smassine
"""

def getKuntarajaMaskFromPalstat(inputfp, kuntakoodi):
    
    """
    A function for clipping kuntaraja mask from MML palstadata.
    
    Parameters
    ----------
    inputfp: <str> <gpd.GeoDataFrame>
        Full input filepath with filename and format (.pkl). E.g. r"C:\Files\etelasavo_palstat.pkl"
    kuntakoodi: <str> or <int>
        Kuntakoodi for the wanted municipality.
    
    Output
    ------
    <shapely.geometry.polygon.Polygon>
        Kuntaraja mask as a Shapely Polygon.
    """
    
    import pickle
    import geopandas as gpd
    from shapely.ops import unary_union
    import sys
    
    with open(inputfp, "rb") as f:
        palstat = pickle.load(f)
    
    if palstat.crs['init'] != 'epsg:3067':
        sys.exit("Your data must have EPSG:3067 (EUREF-TM35FIN) as CRS!")
    
    master_df = gpd.GeoDataFrame(columns=["geometry"], geometry="geometry", crs={'init': 'epsg:3067'})
    
    i = 1
    
    for index, row in palstat.iterrows():
        
        print("Processing kuntarajamaski: " + str(i) + "/" + str(len(palstat)))
        
        if row['properties']['kiinteistotunnuksenEsitysmuoto'][0:3] == str(kuntakoodi):
            row_schema = {'geometry': row.geometry}
            master_df = master_df.append(row_schema, ignore_index=True)
        
        i = i + 1
        
    dis_list = list(master_df['geometry'])
    dissolve = unary_union(dis_list)
    
    return(dissolve)
