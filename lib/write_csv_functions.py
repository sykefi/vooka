import csv
import os
from dictionaries.document_type import tyyppi_maarays


def list_documents(path, folder):
    list_of_documents = []
    kunta_numero = folder
    kunta_numero_path = os.path.join(path, folder)
    for subfolder in os.listdir(kunta_numero_path):
        kaavalaji = subfolder
        kaavalaji_path = os.path.join(kunta_numero_path, kaavalaji)
        for item in os.listdir(kaavalaji_path):
            pdf_item = item
            pdf_document_type = define_document_type(pdf_item, tyyppi_maarays)
            list_of_documents.append([str(kunta_numero), str(""), str(""), str(pdf_item),str(""), str(""), str(kaavalaji), str("FALSE"), str(pdf_document_type)])
    return list_of_documents
    

def store_data_to_list(path):
    folders= []
    combined_pdfnimi_lista = []
    for folder in os.listdir(path):
        try:
            int(folder)
            folders.append(folder)
            kaavatiedot = list_documents(path, folder)
            combined_pdfnimi_lista.extend(kaavatiedot)
            
        except(ValueError):
            continue
    folders_string = '_'.join(folders)
    return combined_pdfnimi_lista, folders_string


# Define a function to check if a filename contains a certain name
def define_document_type(filename, tyyppi_maarays):
    for word in tyyppi_maarays:
        if word in filename:
            return 3
    return 1


def write_csv(file_path, data):
    # Writing data to the CSV file
    with open(file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=';')
        csv_writer.writerows(data)
    