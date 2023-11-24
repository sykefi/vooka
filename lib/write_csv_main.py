import csv
import os

from write_csv_functions import store_data_to_list, write_csv

def main():
    kaava_asiakirja_list, processed_kunnat = store_data_to_list(path_to_folder)
    write_csv(f"{file_path}kaavatiedot_{processed_kunnat}.csv", kaava_asiakirja_list)
    print(f"CSV file {file_path}kaavatiedot_{processed_kunnat} created successfully.")

if __name__ == "__main__":
    main()