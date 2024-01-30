# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 13:24:17 2022

@author: smassine
"""

def snapKuntakaavaToKuntaraja(kaavadata, palstadata, kuntakoodi, tolerance, fill_holes=True, remove_exclaves=False, kuntakoodi_remove_enclave=None):
    
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
            Enonkoski: no data
            Hirvensalmi: 0.00009
            Juva: 0.015
            Kangasniemi: 0.015
            Mikkeli: 0.005
            Mäntyharju: 0.015
            Pertunmaa: 0.0005
            Pieksämäki: no data
            Puumala: 0.015
            Rantasalmi: 0.015
            Sulkava: 0.0005
            Savonlinna: 0.05
            
        Best threshold values in Pohjois-Savo ELY identified in VOOKA project (PLEASE USE):
            Iisalmi: 0.05
            Joroinen: 0.015
            Kaavi: 0.015
            Keitele: 0.015
            Kiuruvesi: 0.015
            Kuopio: 0.0005
            Lapinlahti: 0.015
            Leppävirta: 0.0005
            Pielavesi: 0.015
            Rautavaara: 0.015
            Rautalampi: 0.015
            Siilinjärvi: 0.015
            Sonkajärvi: 0.015
            Suonenjoki: 0.015
            Tervo: 0.015
            Tuusniemi: 0.05
            Varkaus: 0.015
            Vesanto: 0.015
            Vieremä: 0.015
            
    Optional parameters
    -------------------
    fill_holes: <boolean>
        True/False (True default)
        Fills Polygon holes in kuntarajamask when True.
    
    remove_exclaves: <boolean>
        True/False (False default).
        Removes small exclaves outside the municipality if True.
        In Etelä-Savo, True is to be used for Rantasalmi.
    
    kuntakoodi_remove_enclave: <str>
        Kuntakoodi for an enclave municipality.
    
    Output
    ------
    <gpd.GeoDataFrame>
        Original kaavadata with updated geometry information (snapped to municipality border)
    """

    from shapely.geometry import MultiPolygon, Polygon
    import geopandas as gpd
    import pandas as pd
    import sys

    holes = fill_holes

    def getKuntarajaMaskFromPalstat(palstadata, kuntakoodi, fill_holes=holes, remove_exclaves=False):
        
        from shapely.ops import unary_union
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

    if kaavadata.crs['init'] != 'epsg:3067':
        sys.exit("Your kaavadata must have EPSG:3067 (EUREF-TM35FIN) as CRS!")
    
    kuntakaava = kaavadata.loc[kaavadata['kuntakoodi'] == str(kuntakoodi)]
    kunta_copy = kuntakaava.copy()
    
    if palstadata.crs['init'] != 'epsg:3067':
        sys.exit("Your palstadata must have EPSG:3067 (EUREF-TM35FIN) as CRS!")
    
    if kuntakoodi_remove_enclave != None:
        geom_kunta = getKuntarajaMaskFromPalstat(palstadata=palstadata, kuntakoodi=kuntakoodi, remove_exclaves=remove_exclaves)
        geom_kunta_2 = getKuntarajaMaskFromPalstat(palstadata=palstadata, kuntakoodi=kuntakoodi_remove_enclave, remove_exclaves=remove_exclaves)
        geom_kunta = geom_kunta.difference(geom_kunta_2)
    else:
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

    muut = kaavadata.loc[kaavadata['kuntakoodi'] != str(kuntakoodi)]
    master = pd.concat([muut, kunta_copy], ignore_index=True)
    
    return(master)
