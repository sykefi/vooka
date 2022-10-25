# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 10:10:23 2022

@author: smassine
"""

def repairDatasetGeometries(data, geom_column):
    
    """
    A function for repairing all Geopandas GeoDataFrame geometries if they are not valid.

    Parameters
    ----------
    data: <geopandas.GeoDataFrame>
        A GeoDataFrame containing Shapely geometries in a geometry column.
    geom_column: <str>
        Name of the geometry column in GeoDataFrame.
    
    Output
    ------
    <geopandas.GeoDataFrame>
        A GeoDataFrame with valid Shapely geometries.
    """
    
    from funktiot.geometry_validity import makeGeometryValid
    from shapely.geometry import MultiPolygon, Polygon, GeometryCollection
    
    data_copy = data.copy()
    data_repaired = makeGeometryValid(data=data, geom_column=geom_column)
    
    for index, row in data_repaired.iterrows():
        
        if type(row[geom_column]) == MultiPolygon:
            None
        elif type(row[geom_column]) == Polygon:
            None
        elif type(row[geom_column]) == GeometryCollection:
            data_repaired.at[index, geom_column] = row[geom_column][0]
        else:
            data_repaired.at[index, geom_column] = data_copy.at[index, geom_column]
            print("Manual repair required for geometry at index: " + str(index) + " (QGIS " + str(index + 1) + ").")
    
    return(data_repaired)
    
