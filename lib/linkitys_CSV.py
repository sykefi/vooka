import geopandas as gpd
import os
from fuzzywuzzy import fuzz, process
import csv

"""
Tämä prosessin suorittamista varten tarvitset seuraavat tiedot sekä prosessia varten sinulla tulee olla kansio, jossa pdf-kaavaliitteet sijaitsevat
mielellään samassa kansiossa kunnan indeksiaineiston (paikkatieto) kanssa. Oletuksena myös CSV-taulukko luodaan samaan työskentely kansioon.

Tarvitset siis:
    
    1. Tiedostopolun kunnan pdf-kaavaliitekansioon
    2. Tiedostpolun kunnan kaavaindeksiaineistoon (paikkatieto). Vain shp- ja gpkg- tiedostoja voidaan lukea
    3. Kansiopolun siihen kansioon mihin haluat tallentaan CSV-taulukon (suositellaan samaa kansiota kuin muutkin tiedot)
    
Ennen koodin ajamista sinun tulee määritellä:
    1. Kuntanumero
    2. Kaavalajin nimi, jonka kanssa työskennellään (ak, rak, yk)
    3. Kaavaindeksin aineiston (paikkatieto) sarake, jossa indeksitunnus sijaitsee
    
HUOM! Mikäli kaavaindeksiä ei ole määritelty aineistolle tätä vaihetta ei tule suorittaa.


Tämä koodi myös täyttää automaattisesti arvion dokumentin tyypistä (1 tai 3), jolloin nämä täytyy manuaalisesti tarkistaa oikeiksi.
    
"""


#Anna kansiopolku missä kaavaliitteet sijaitsevat

kaavaliitteet = 'C:/Users/EmiliaTimlin/Documents/Meneillaan_olevat_Projektit/PohjoissavoVooka/testikansio_14/ak'


#Anna kansiopolku missä kunnan indeksiaineisto sijaitsee

kunta_kaavaindeksi = 'C:/Users/EmiliaTimlin/Documents/Meneillaan_olevat_Projektit/PohjoissavoVooka/testikansio_14/asemakaava_kuopio_etrs_gk27_epsg_3881.gpkg'

#Anna kuntanumero

kunta_numero = 297

#Anna kaavalajin nimi

kaavalaji = "ak"

#Anna sarakkeen nimi, jossa indeksitieto sijaitsee
indeksi_sarake = 'TUNNUS'

#Laita tähän sen kansion polku, johon haluat saada kaavatiedot.
directory = 'C:/Users/EmiliaTimlin/Documents/Meneillaan_olevat_Projektit/PohjoissavoVooka/testikansio_14'


#Tässä on lista, jonka perusteella funktio määrittelee onko tiedosto kaavakartta vai määräys. Tätä listaa voi tarpeen tullen muokata
#on myös hyvä huomioida, että tämä lista ei anna 100% tarkkoja tuloksia, eli tiedostojen tyyppi täytyy vielä varmistaa manuaalisesti
dokumentin_tyyppi_maarays = ["maaraykset", "merkinnat", "selostus", "merkinnät", "määräykset"]



def open_gdf(file_path, index_id):
    gdf = gpd.read_file(file_path)
    gdf[index_id] = gdf[index_id].astype(str)
    column_values = gdf[index_id].tolist()
    return column_values


def contains_name_in_filename(filename, words):
    for word in words:
        if word in filename:
            return 3
    return 1

    
def loop(path, pdfnimi_lista=[]):
    for item in os.listdir(path):
        pdf_item = item
        pdfnimi_lista.append(pdf_item)
    return pdfnimi_lista
    


def find_best_matches(list1, list2, threshold=40):
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


def make_csv(matches, linkitys_tiedot=[]):
    x = 0
    for i in matches:
        dokumentin_tyyppi = contains_name_in_filename(i, dokumentin_tyyppi_maarays)
        if i == matches[i]:
            linkitys_tiedot.append([str(kunta_numero), str(""), str(""), str(i),str(""), str(""), str(kaavalaji), str("FALSE"), str(dokumentin_tyyppi),str("")])
        else:
            x += 1
            linkitys_tiedot.append([str(kunta_numero), str(matches[i][0]), str(""), str(i),str(""), str(""), str(kaavalaji), str("FALSE"), str(dokumentin_tyyppi), str(matches[i][1])])
    print("Found " + str(x) + " matches.")
    return linkitys_tiedot


def write_csv(file_path, data):
    # Writing data to the CSV file
    with open(file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=';')
        csv_writer.writerows(data)
    
    print(f"CSV file '{file_path}' created successfully.")


def main():
    kaavaindeksit = open_gdf(kunta_kaavaindeksi, indeksi_sarake)
    
    kaavat = loop(kaavaliitteet)
    
    linkitys = find_best_matches(kaavat, kaavaindeksit)
    
    tee_csv = make_csv(linkitys)
        
    write_csv(f"{directory}/kaavatiedot_{kunta_numero}_{kaavalaji}.csv", tee_csv)   

if __name__ == "__main__":
    main()


