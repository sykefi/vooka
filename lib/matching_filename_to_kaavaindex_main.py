import geopandas as gpd
import os
from fuzzywuzzy import fuzz, process
import csv

from matching_filename_to_kaavaindex_functions import open_gdf, list_documents, match_filename_to_kaavaindex, structure_CSV_base, write_csv
from dictionaries.document_type import tyyppi_maarays

    
def main():
    
    
    kaavaindex_list = open_gdf(kunta_kaavaindeksi, indeksi_sarake)
    
    kaava_asiakirja_list = list_documents(kaava_asiakirjat)
    
    match_filename_to_kaavaindex_result = match_filename_to_kaavaindex(kaava_asiakirja_list, kaavaindex_list)
    
    csv = structure_CSV_base(match_filename_to_kaavaindex_result, kunta_numero, kaavalaji)
        
    write_csv(f"{directory}/kaavatiedot_{kunta_numero}_{kaavalaji}.csv", csv)   

if __name__ == "__main__":
    main()
