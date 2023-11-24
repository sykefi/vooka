import geopandas as gpd
import os
from fuzzywuzzy import fuzz, process
import csv

from dictionaries.document_type import tyyppi_maarays



def open_gdf(file_path, index_id):
    #Open gpkg or shp file
    gdf = gpd.read_file(file_path)
    #Select column
    gdf[index_id] = gdf[index_id].astype(str)
    #Get values from column to list
    column_values = gdf[index_id].tolist()
    return column_values


def define_document_type(filename, tyyppi_maarays):
    #Check if value exist in wordlist
    for word in tyyppi_maarays:
        if word in filename:
            return 3
    return 1

    
def list_documents(path, pdfnimi_lista=[]):
    #Loop filenames from folder to list
    for item in os.listdir(path):
        pdf_item = item
        pdfnimi_lista.append(pdf_item)
    return pdfnimi_lista
    


def match_filename_to_kaavaindex(list1, list2, threshold=35):
    #If value match item in indexlist
    best_matches = {}
    matches_dict = {}
    for item1 in list1:
        itemrep = item1.replace(".pdf", "")
        match, score = process.extractOne(itemrep, list2, scorer=fuzz.ratio)
        if score >= threshold:
            best_matches[item1] = (match, score)
            matches_dict[item1] = (match, score)
        else:
            matches_dict[item1] = item1
    return matches_dict


def structure_CSV_base(matches, kunta_numero, kaavalaji, linkitys_tiedot=[]):
    #Form structure of CSV
    matches_count = 0
    for i in matches:
        dokumentin_tyyppi = define_document_type(i, tyyppi_maarays)
        if i == matches[i]:
            linkitys_tiedot.append([str(kunta_numero), str(""), str(""), str(i),str(""), str(""), str(kaavalaji), str("FALSE"), str(dokumentin_tyyppi),str("")])
        else:
            matches_count += 1
            linkitys_tiedot.append([str(kunta_numero), str(matches[i][0]), str(""), str(i),str(""), str(matches[i][1]), str(kaavalaji), str("FALSE"), str(dokumentin_tyyppi)])
    print("Found " + str(matches_count) + " matches.")
    return linkitys_tiedot


def write_csv(file_path, data):
    # Writing data to the CSV file
    with open(file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=';')
        csv_writer.writerows(data)
    
    print(f"CSV file '{file_path}' created successfully.")
    

