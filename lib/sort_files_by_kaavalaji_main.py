

from sort_files_by_kaavalaji import get_folders_from_directory, CaseInsensitiveDict, match_folder_into_names_in_dictionary_and_call_make_folder,call_copy_folders
from dictionaries.kaavalaji_names import kaavalaji_nimet
from dictionaries.kuntakoodit import kuntakoodi



def main():
    folders_from_chosen_direcotry=get_folders_from_directory(valittu_kansio)
    case_insensitive_dict = CaseInsensitiveDict(kuntakoodi)
    key = match_folder_into_names_in_dictionary_and_call_make_folder(case_insensitive_dict, folders_from_chosen_direcotry, valittu_kansio)
    case_insensitive_dict_kansionimet = CaseInsensitiveDict(kaavalaji_nimet)        
    call_copy_folders(key, case_insensitive_dict_kansionimet, valittu_kansio)
    print("Kansiolajittelu onnistui")

if __name__ == "__main__":
    main()