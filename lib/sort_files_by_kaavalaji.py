
import os
import shutil
from collections import UserDict


from dictionaries.kaavalaji_names import kaavalaji_nimet
from dictionaries.kuntakoodit import kuntakoodi



"""
1. Käsittele nimet niin, että ne eivät ole "case sensitive"
"""

class CaseInsensitiveDict(UserDict):
    def __setitem__(self, key, value):
        self.data[self._normalize_key(key)] = value

    def __getitem__(self, key):
        return self.data[self._normalize_key(key)]

    def __delitem__(self, key):
        del self.data[self._normalize_key(key)]

    def __contains__(self, key):
        return self._normalize_key(key) in self.data

    def _normalize_key(self, key):
        return key.lower()

"""
2. Luo uusi kansio, joka nimetty (kuntakoodi).
"""

def get_folders_from_directory(directory_path):
    # Tee lista kaikista kansioista ja tiedostoista kyseisen kansion sisällä
    all_items = os.listdir(directory_path)
    # Listaa vain kansiot
    folders = [item for item in all_items if os.path.isdir(os.path.join(directory_path, item))]
    return folders
    
def make_new_folder(parent_dir, new_folder_name):
    # Muodosta tiedostopolku
    path = os.path.join(parent_dir, new_folder_name)
    # Luo uusi kansio
    try:
        os.mkdir(path)
    except OSError as error:
        print("Kansion luominen epäonnistui" + str(error)) 

def match_folder_into_names_in_dictionary_and_call_make_folder(keys, folders, parent_dir):
    # Tee tuple-lista, jossa tietoina kunnan nimi ja vastaava kuntakoodi
    my_tuple_list = []
    for folder in folders:
        if folder in keys:
            #print(folder)
            key=str(keys[folder])
            #print(key)
            # Tee uusi kansio kunnan nimeä vastaavalla kuntakoodilla
            make_new_folder(parent_dir, key)
            my_tuple_list.append((folder, key))
    return my_tuple_list
            
"""
#3. Kansiorakenteen luominen.
"""

def loop_folders(path, destination):
    # Tällä funktiolla käydään läpi ne kansiot, jotka ovat asemakaava-, ranta-asemakaava- ja yleiskaava -kansioiden alla
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            loop_folders(item_path, destination)
        elif item.endswith(".pdf"):
            #Jos alikansioissa on pdf-tiedostoja, niin ne lisätään uusiin kansioihin
            file_dest = os.path.join(destination, item)
            shutil.copyfile(item_path, file_dest)

def copy_pdf_folders(src_folder, dest_folder, rename_dict):
    for folder in os.listdir(src_folder):
        source_folder_path = os.path.join(src_folder, folder)
        if os.path.isdir(source_folder_path) and folder in rename_dict:
            new_folder_name = rename_dict.get(folder, folder)
            dest_folder_path = os.path.join(dest_folder, new_folder_name)
            shutil.copytree(source_folder_path, dest_folder_path, ignore=ignore_non_pdf)
            for subfolder in os.listdir(source_folder_path):
                subfolder_path = os.path.join(source_folder_path, subfolder)
                if os.path.isdir(subfolder_path):
                    loop_folders(subfolder_path, dest_folder_path)

def ignore_non_pdf(folder, contents):
    return [file for file in contents if not file.endswith(".pdf")]

def call_copy_folders(tuple_list, lista_alikansioista, tyoskentely_kansio):
    for item in tuple_list:
        orig = item[0]
        original_source = str(tyoskentely_kansio) + "/" + str(orig)
        dest = item[1]
        destination_location = str(tyoskentely_kansio) + "/" + str(dest)
        copy_pdf_folders(original_source, destination_location, kaavalaji_nimet)
