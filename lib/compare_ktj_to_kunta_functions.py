
import pandas as pd
import sys
import geopandas as gpd
from shapely.geometry import Polygon, LineString, Point, MultiPolygon , MultiLineString, MultiPoint
import difflib
import pandas as pd

import warnings
warnings.filterwarnings("ignore")



"""
Tähän pitää luoda vaan yhteys.
"""

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

"""
Kaikki tätä ennen importataan.
"""


def compare_items(item1, item2):
    if pd.isna(item1):
        if pd.isna(item2):
            return "Puuttuu kaikista"
        else:
            return "Puuttuu kunnan KTJ"
    else:
        if pd.isna(item2):
            return "Puuttuu kunnan aineistosta"
        else:
            # Add additional specific comparison logic here if needed
            return True

def check_existence(item1, item2):
    value = None  # Provide a default value
    
    if item1 is None:
        if item2 is None:
            value = 'Voimpvm puuttuu molemmista'
        else:
            value = 'Voimpvm puuttuu KTJ'
    
    return value

def check_equality(column_value_1, column_value_2):
    if column_value_1 == column_value_2:
        return True
    else:
        return False


def iou_and_delta_to_columns(geom1, geom2):

    
    iou = calculate_iou(geom1, geom2)

    
    pattern = get_DE9IM_pattern(geom1, geom2)
    
    topo_equal = topologically_equal_DE9IM(geom1, geom2)
    if topo_equal == False:
        if iou >= 98:
            topo_equal = True
            
    refe_area = geom2.area / 10000
    
    try:
        delta = round(((refe_area - (geom1.area / 10000)) / (geom1.area / 10000)) * 100, 2)
    except TypeError:
        delta = None

    return pattern, iou, topo_equal, delta, refe_area
    


def initialize_columns(df, column_names, default_value=None):
    for column_name in column_names:
        df[column_name] = default_value


def check_CRS(layer1, layer2):
    if layer1.crs != layer2.crs:
        # If not, raise an exception
        raise ValueError("Your data must have the same coordinate reference system!")


def filter_data(df, kuntanimi, kaavalajit):
    filtered_data = df.loc[df['kuntanimi'] == kuntanimi]
    filtered_data = filtered_data.loc[filtered_data['kaavalaji'].isin(kaavalajit)]
    return filtered_data



def trim(string):
    delimiter = "§"
    stripped_string = string.split(delimiter)[0]
    return stripped_string

def compare_and_return_match(item1, item2, threshold=0.35):
    #print(item1)
    #print(item2)
    if pd.isna(item2):
        return "Puuttuu kunnan aineistosta"
    similarity_ratio = difflib.SequenceMatcher(None, item1, item2).ratio()
    #print(f"Similarity ratio:{similarity_ratio}")
    # Check if the similarity ratio exceeds the threshold
    if similarity_ratio > threshold:
        
        return 1
    else:
        return 0  # or any other value you prefer for non-matching case
    
    


def get_DE9IM_pattern(geom1, geom2):
    pattern = geom1.relate(geom2)
    return(pattern)

def topologically_equal_DE9IM(geom1, geom2):
    # Two geometries are topologically equal if their interiors intersect and no part of the interior or boundary of one geometry intersects the exterior of the other.
    # DE-9IM pattern: "T*F**FFF*"
    equals = geom1.relate_pattern(geom2, 'T*F**FFF*')
    return(equals)

def calculate_iou(geom1, geom2):
    iou = round((geom1.intersection(geom2).area / geom1.union(geom2).area)*100, 2)
    return(iou)

