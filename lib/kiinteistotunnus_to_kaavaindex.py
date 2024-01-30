# -*- coding: utf-8 -*-

def kiinteistotunnusToKaavaIndex(kiinttunnus_data, kaava_data):
    
    """
    A Function for assigning kaavatunnus information to each kaavaindex.
    
    Parameters
    ----------
    kiinttunnus_data: <gpd.GeoDataFrane>
        Kiinteistötunnus data as a geopandas GeoDataFrame.
    kaava_data: <gpd.GeoDataFrane>
        Kaavadata as a geopandas GeoDataFrame.
            
    Output
    ------
    <GeoDataFrame>
        Combined data as a geopandas GeoDataFrame.
    """    
    
    import sys
    import geopandas as gpd
    from shapely.geometry import box
    
    try:
        # Check to see if kaava and kiinteistötunnus data have the same CRS system
        if kaava_data.crs['init'] != kiinttunnus_data.crs['init']:
            # If not, comparison cannot be made. Sys exit.
            sys.exit("Your data must have the same coordinate reference system!")
    except KeyError:
        sys.exit("Your data must have the same coordinate reference system!")
    
    # Define bbox for kiinteistotunnukset based on kaavadata
    bounds = kaava_data.total_bounds
    if any(map(lambda x: x is None, bounds)):
        # Handle the case where bounds are empty
        raise ValueError("Bounding box coordinates are empty.")
    bbox = box(*bounds)
    
    # Clip kiinteistotunnukset data with bbox
    kiinttunnus_data['intersect'] = None
    
    i = 1
    
    for index, row in kiinttunnus_data.iterrows():
        
        print("Processing: " + str(i) + "/" + str(len(kiinttunnus_data)))
        
        if row['geometry'].intersects(bbox) == True:
            kiinttunnus_data.at[index, 'intersect'] = 'True'
        
        i = i + 1
        
    kunta_kiinttunnus = kiinttunnus_data.loc[kiinttunnus_data['intersect'] == 'True']
    kunta_kiinttunnus = kunta_kiinttunnus.drop(columns=['intersect'])
    
    # Loop through kaavaindexes and kiinteistötunnukset to see which kiinteistötunnukset are inside each kaavaindex
    kaava_data['kiinttunnus'] = None
    i = 1
    
    for index, row in kaava_data.iterrows():
        
        print("------------------------------------------------------")
        print("Processing: " + str(i) + "/" + str(len(kaava_data)))
        print("------------------------------------------------------")
        
        kaava = row
        kiinttunnus_list = []
        
        for idx, row in kunta_kiinttunnus.iterrows():
            
            if row['geometry'].within(kaava['geometry']):
                print("Kiinteistötunnus found within kaavaindex!")
                kiinttunnus_list.append(row.kiinteistotunnus)
        
        if len(kiinttunnus_list) != 0:
            kaava_data.at[index, 'kiinttunnus'] = str(kiinttunnus_list)
        
        i = i + 1

    return(kaava_data)