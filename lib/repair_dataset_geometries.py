# -*- coding: utf-8 -*-
"""
Functions for repairing datasets in the VOOKA ETL process.
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
    
    Returns
    ------
    <geopandas.GeoDataFrame>
        A GeoDataFrame with valid Shapely geometries.
    """

    from shapely.validation import make_valid
    from shapely.geometry import MultiPolygon, Polygon, GeometryCollection

    def makeValid(data, geom_column):
        data[geom_column] = data.apply(lambda row: make_valid(row[geom_column]) if not row[geom_column].is_valid else row[geom_column], axis=1)
        return(data)
    
    data_copy = data.copy()
    data_repaired = makeValid(data=data, geom_column=geom_column)
    
    for index, row in data_repaired.iterrows():
        
        if type(row[geom_column]) == MultiPolygon:
            None
        elif type(row[geom_column]) == Polygon:
            None
        elif type(row[geom_column]) == GeometryCollection:
            data_repaired.at[index, geom_column] = row[geom_column][0]
            print("GeometryCollection extracted!")
        else:
            data_repaired.at[index, geom_column] = data_copy.at[index, geom_column]
            print("Manual repair required for geometry at index: " + str(index) + " (QGIS " + str(index + 1) + ").")
    
    return(data_repaired)


def removeUnnecessaryVertices(data, geom_column, tolerance=0.001):
    
    """
    A function for removing unnecessary vertices within a straight line.
    Utilizes Shapely's simplify-function and preserves topology. 
    
    Parameters
    ----------
    data: <geopandas.GeoDataFrame>
        A GeoDataFrame containing Shapely geometries in a geometry column.
    geom_column: <str>
        Name of the geometry column in the GeoDataFrame.
    tolerance: <float or array_like>
        By default 0.001.
        The maximum allowed geometry displacement. 
        The higher this value, the smaller the number of vertices in the 
        resulting geometry.

    Returns
    -------
    <geopandas.GeoDataFrame>
        A GeoDataFrame in which extra vertices on a straight line 
        have been removed.

    """
            
    data[geom_column] = data.simplify(tolerance)
    
    print("Extra vertices have been succesfully removed.")
    
    return data
