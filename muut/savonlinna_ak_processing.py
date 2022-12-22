# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 09:36:37 2022

@author: smassine
"""

import geopandas as gpd
import pandas as pd
from fiona.crs import from_epsg

input_fp_kaava = r""
input_fp_points = r""
input_layer_kaava = ""
input_layer_points = ""

outfp = r".gpkg"
out_layer = ""

# Read necessary data
sln_kaava = gpd.read_file(input_fp_kaava, layer=input_layer_kaava)
sln_points = gpd.read_file(input_fp_points, layer=input_layer_points)

### 1. MERGE BY ID
# Ignore rows that couldn't be assigned to any Polygon
points = sln_points.loc[sln_points['id_ei_voitu_maarittaa'].isnull()]
# Ignore rows that are to be spatially joined later
points = points.loc[~points['aluerajaid'].isnull()]

# Change ID columns to integer and name them similarly
points = points.astype({"aluerajaid": int})
points = points.rename(columns= {'aluerajaid': 'id'})
kaavat = sln_kaava.astype({"id": int})

# Merge layers
points_dis = points.dissolve(by='id')
points_dis.reset_index(inplace=True)
points_dis = points_dis.drop('geometry', axis=1)

merged = pd.merge(kaavat, points_dis, on="id", how="left")

# Define crs
merged.crs = from_epsg(3883)

### 2. SPATIAL JOIN
# Ignore unnecessary rows
spatial_points = sln_points.loc[sln_points['aluerajaid'].isnull()]
spatial_points = spatial_points.loc[spatial_points['id_ei_voitu_maarittaa'].isnull()]

# Spatial join
def spatialJoinAttributes(poly_data, point_data, column):
    
    for index, row in poly_data.iterrows():
        
        for idx, rivi in point_data.iterrows():
            
            if rivi['geometry'].within(row['geometry']):
                poly_data.at[index, column] = rivi[column]
                print("Assinged!")
                break
            
    return(poly_data)

hyvaksyja = spatial_points.loc[~spatial_points['hyvaksyja'].isnull()]
hyvaksymispvm = spatial_points.loc[~spatial_points['hyvaksymis'].isnull()]
kaavatunnus = spatial_points.loc[~spatial_points['kaavatunnu'].isnull()]
nimi = spatial_points.loc[~spatial_points['nimi'].isnull()]
area = spatial_points.loc[~spatial_points['pintaAla'].isnull()]

merged = spatialJoinAttributes(merged, hyvaksyja, 'hyvaksyja')
merged = spatialJoinAttributes(merged, hyvaksymispvm, 'hyvaksymis')
merged = spatialJoinAttributes(merged, kaavatunnus, 'kaavatunnu')
merged = spatialJoinAttributes(merged, nimi, 'nimi')
merged = spatialJoinAttributes(merged, area, 'pintaAla')

# Project geometries to TM35
merged_proj = merged.to_crs(epsg=3067)

# Drop unnecessary columns
merged_pro = merged_proj.drop('id_ei_voitu_maarittaa', axis=1)

### 3. DROP GHOST GEOMETRIES
drop_list = []

for index, row in merged_pro.iterrows():
    if row.kaavatunnu == None and row.hyvaksymis == None:
        drop_list.append(index)

merged_pro_filtered = merged_pro.drop(drop_list)
        
# Save
merged_pro_filtered.to_file(outfp, layer=out_layer, driver="GPKG")
