# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 13:24:17 2022

@author: smassine
"""

import geopandas as gpd
from shapely.geometry import MultiPolygon, Polygon
import sys
from funktiot.accessory_functions import readPickleData, getKuntarajaMaskFromPalstat, saveGPKG

def snapKuntakaavaToKuntaraja(kaavadata, palstadata, kuntakoodi, tolerance, remove_exclaves=False):
    
    """
    Parameters
    ----------
    kaavadata: <gpd.GeoDataFrame>
        Input (yleis)kaavadata as a Geopandas Geodataframe.
    palstadata: <gpd.GeoDataFrame>
        Input MML palstadata as a Geopandas Geodataframe.
    kuntakoodi: <str> or <int>
        Kuntakoodi for the wanted municipality.
    tolerance: <float>
        Tolerance value to filter out unwanted difference indices.
        
        Best threshold values in Etelä-Savo ELY identified in VOOKA project (PLEASE USE):
            Juva: 0.015
            Kangasniemi: 0.015
            Mikkeli: 0.005
            Mäntyharju: 0.015
            Pertunmaa: 0.0005
            Puumala: 0.015
            Rantasalmi: 0.015
            Sulkava: 0.0005
            <TO BE CONTINUED>
            
    Optional parameters
    -------------------
    remove_exclaves <boolean>
        True/False (False default).
        Removes small exclaves outside the municipality if True.
        In Etelä-Savo, True is to be used for Rantasalmi.
    
    Output
    ------
    <gpd.GeoDataFrame>
        Original kaavadata with updated geometry information (snapped to municipality border)
    """
    
    if kaavadata.crs['init'] != 'epsg:3067':
        sys.exit("Your kaavadata must have EPSG:3067 (EUREF-TM35FIN) as CRS!")
    
    kuntakaava = kaavadata.loc[kaavadata['kuntakoodi'] == str(kuntakoodi)]
    kunta_copy = kuntakaava.copy()
    
    if palstadata.crs['init'] != 'epsg:3067':
        sys.exit("Your palstadata must have EPSG:3067 (EUREF-TM35FIN) as CRS!")
    
    geom_kunta = getKuntarajaMaskFromPalstat(palstadata=palstadata, kuntakoodi=kuntakoodi, remove_exclaves=remove_exclaves)
    
    i = 1
    
    for index, row in kunta_copy.iterrows():
        
        master_df = gpd.GeoDataFrame(columns=["geometry"], geometry="geometry", crs={'init': 'epsg:3067'})
        
        print("Processing " + str(i) + "/" + str(len(kunta_copy)))
        geom_kaava = row['geometry']
        
        if geom_kaava.within(geom_kunta) == False:
        
            intersection = geom_kaava.intersection(geom_kunta)
            difference_kunta = geom_kunta.difference(geom_kaava)
            
            if type(geom_kaava) == MultiPolygon:
                kaavapalat = list(geom_kaava)
            
            if type(difference_kunta) == MultiPolygon:
                polygons = list(difference_kunta)
    
                for polygon in polygons:
                    
                    if type(geom_kaava) == Polygon:
                    
                        if polygon.within(Polygon(geom_kaava.exterior)):
                            print("Dismiss by location (Polygon)")
                        elif polygon.area > geom_kaava.area * float(tolerance):
                            print("Dismiss by area (Polygon)")
                        else:
                            row_schema = {'geometry': polygon}
                            master_df = master_df.append(row_schema, ignore_index=True)
                    
                    elif type(geom_kaava) == MultiPolygon:
                        
                        for pala in kaavapalat:
                            
                            if polygon.within(Polygon(pala.exterior)):
                                print("Dismiss by location (MultiPolygon)")
                                break
                            elif polygon.area > geom_kaava.area * float(tolerance):
                                print("Dismiss by area (MultiPolygon)")
                                break
                            elif pala == kaavapalat[len(kaavapalat)-1]:
                                row_schema = {'geometry': polygon}
                                master_df = master_df.append(row_schema, ignore_index=True)
                            else:
                                None
                    else:
                        sys.exit("Kaava geometry has to be either type Polygon or MultiPolygon!")
    
            elif type(difference_kunta) == Polygon:
                
                if type(geom_kaava) == Polygon:
                    
                    if difference_kunta.within(Polygon(geom_kaava.exterior)):
                        print("Dismiss by location (Polygon)")
                    elif difference_kunta.area > geom_kaava.area * float(tolerance):
                        print("Dismiss by area (Polygon)")
                    else:
                        row_schema = {'geometry': difference_kunta}
                        master_df = master_df.append(row_schema, ignore_index=True)
                    
                elif type(geom_kaava) == MultiPolygon:
                    
                    for pala in kaavapalat:
                            
                        if difference_kunta.within(Polygon(pala.exterior)):
                            print("Dismiss by location (MultiPolygon)")
                            break
                        elif difference_kunta.area > geom_kaava.area * float(tolerance):
                            print("Dismiss by area (MultiPolygon)")
                            break
                        elif pala == kaavapalat[len(kaavapalat)-1]:
                            row_schema = {'geometry': difference_kunta}
                            master_df = master_df.append(row_schema, ignore_index=True)
                        else:
                            None
    
            else:
                sys.exit("Kaava geometry has to be either type Polygon or MultiPolygon!")
    
            poly_list = list(master_df['geometry'])
            multi_difference = MultiPolygon(poly_list)
            
            union = intersection.union(multi_difference)
            
            kunta_copy.at[index, 'geometry'] = union
            
        i = i + 1
    
    return(kunta_copy)

palstat = readPickleData(inputfp=r"<insert filepath here>.pkl")
kaava_data = gpd.read_file(r"<insert filepath here>.gpkg", layer="<insert layer name here>")

kunta_snapped = snapKuntakaavaToKuntaraja(kaavadata=kaava_data,
                                                 palstadata=palstat,
                                                 kuntakoodi='<insert kuntakoodi here>',
                                                 tolerance=0.015) #Change according to municipality !! Add remove_exclaves if necessary !!

saveGPKG(kunta_snapped, outputfp=r"<insert filepath here>.gpkg", layer_name="<insert layer name here>")
