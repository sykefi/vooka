# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 11:02:24 2022

@author: smassine
"""

from shapely.geometry import Polygon, LineString, Point, MultiPolygon , MultiLineString, MultiPoint

def get_DE9IM_pattern(geom1, geom2):
    
    """
    A Function for getting a DE-9IM topological pattern for two Shapely geometries.
    
    Parameters
    ----------
    geom1, geom2: <shapely.geometry>
        A Shapely geometry. Either Point, LineString, Polygon, MultiPoint, MultiLineString, or MultiPolygon.
    
    Output
    ------
    <str>
        A DE-9IM matrix as a string.
    """
    
    pattern = geom1.relate(geom2)
    
    return(pattern)
    
def topologically_equal_DE9IM(geom1, geom2):
    
    """
    A Function for checking if two Shapely geometries are topologically equal.
    
    Parameters
    ----------
    geom1, geom2: <shapely.geometry>
        A Shapely geometry. Either Point, LineString, Polygon, MultiPoint, MultiLineString, or MultiPolygon.
    
    Output
    ------
    <boolean>
        True/False answer to topological equality.
    """
    
    # Two geometries are topologically equal if their interiors intersect and no part of the interior or boundary of one geometry intersects the exterior of the other.
    # DE-9IM pattern: "T*F**FFF*"
    equals = geom1.relate_pattern(geom2, 'T*F**FFF*')
    
    return(equals)


def calculate_iou(geom1, geom2):

    """
    A Function to calculate an intersection of union (iou) for two Shapely Polygons.
    
    Parameters
    ----------
    geom1, geom2: <shapely.geometry>
        A Shapely geometry. Either Polygon or MultiPolygon.
    
    Output
    ------
    <float>
        An iou as a percentage between two Shapely Polygons rounded to two decimals.
    """
    
    iou = round((geom1.intersection(geom2).area / geom1.union(geom2).area)*100, 2)
    
    return(iou)
