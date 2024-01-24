import os
import requests
import pandas as pd

from lib.accessory_functions import download_file, create_folder
     
def main():

    folder_exist = create_folder(download_dir)
    if folder_exist == False:
        return
    
    # Read the entire CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file, sep=';', encoding='utf-8')

    # Specify the columns you want to select (e.g., columns 'Column1' and 'Column3')
    selected_column_name = [column_name]

    # Use DataFrame indexing to select the desired column
    selected_column = df[selected_column_name]

    #selected_column_values = df[selected_column_name].values.tolist()
    selected_rows = df[column_name].tolist()
    
    # Download each file from the list of URLs
    for url in selected_rows:
        filename = os.path.basename(url)
        save_path = os.path.join(download_dir, filename)
        download_file(url, save_path)
    
    print("Operaatio valmis")

if __name__ == "__main__":
    main()

