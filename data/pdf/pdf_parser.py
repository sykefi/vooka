# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 10:31:35 2022

@author: smassine
"""

import pandas as pd
import geopandas as gpd
import sys

data = pd.read_csv(r"G:\Oma Drive\Liiketoiminta\Suomen ympäristökeskus\VOOKA\Python\PDF-linkityskonversio - Master.csv", delimiter=',',  usecols = [i for i in range(12)])
kaava_data = gpd.read_file(r"G:\Jaetut Drivet\Liiketoiminta\Suomen ympäristökeskus\Voimassa olevat kaavat rakennetun ympäristön tietojärjestelmään -pilotti (VOOKA)\Projekti\02_lähtötiedot\Yhdistetyt kaavatiedot\gpkg-korjattu\master-refined.gpkg", layer="asemakaavat_kunta")

def declareMultipage(data, master_dir, kuntakoodi, kaavalaji):
    
    import glob, os
    import PyPDF2
    
    data_copy = data.copy()
    
    folder = os.path.join(master_dir, kuntakoodi, kaavalaji)
    os.chdir(folder)
    
    filelist = glob.glob("*.pdf")
    
    pala = data.loc[data['Kunta'] == float(kuntakoodi)]
    pala = pala.loc[pala['Kaavalaji'] == kaavalaji]
        
    i = 1
    
    for index, row in pala.iterrows():
        
        print("Processing " + str(i) + "/" + str(len(pala)))
        
        for file in filelist:
        
            try:
                pdf = open(file, 'rb')
                readpdf = PyPDF2.PdfFileReader(pdf)
                totalpages = readpdf.numPages
                    
            except FileNotFoundError:
                totalpages = 1
                
            if row['Original filename'] == file:
                
                if totalpages == 1: 
                    data_copy.at[index, 'Multipage'] = False
                elif totalpages == 0:
                    None
                else:
                    data_copy.at[index, 'Multipage'] = True
                break
        
        i = i + 1
    
    return(data_copy)

testi = declareMultipage(data=data,
                         master_dir=r"G:\Jaetut Drivet\Liiketoiminta\Suomen ympäristökeskus\Voimassa olevat kaavat rakennetun ympäristön tietojärjestelmään -pilotti (VOOKA)\Projekti\02_lähtötiedot\Yhdistetyt kaavatiedot\documents\Ladatut",
                         kuntakoodi="740",
                         kaavalaji="ak")


## PDF-LINKITTÄJÄ ALLA (VAIHEESSA!)

def joinPDFsToKaavadata(kaavadata, link_table, kuntakoodi, kaavalaji):

    link_pala = link_table.loc[link_table['Kunta'] == float(kuntakoodi)]
    link_pala = link_pala.loc[link_pala['Kaavalaji'] == kaavalaji]
    link_pala = link_pala.loc[link_pala['Tila'] == 'ok'] #selivitettävä myöhemmässä vaiheessa vielä 'ei ok' rivit
    
    kaava_pala = kaavadata.loc[kaavadata['kuntakoodi'] == kuntakoodi]
    
    # https://koodistot.suomi.fi/codescheme;registryCode=rytj;schemeCode=RY_Kaavalaji
    if kaavalaji == 'ak':
        kaava_pala = kaava_pala.loc[kaava_pala['kaavalaji'].isin(['31', '32', '35', '39'])]
    elif kaavalaji == 'rak':
        kaava_pala = kaava_pala.loc[kaava_pala['kaavalaji'].isin(['33', '34'])]
    elif kaavalaji == 'yk':
        kaava_pala = kaava_pala.loc[kaava_pala['kaavalaji'].isin(['21', '22', '23', '24', '25', '26'])]
    else:
        sys.exit("Kaavalaji must be either 'ak', 'rak' or 'yk'!")
    
    copy_kaavapala = kaava_pala.copy()
    
    i = 1
    
    for index, row in kaava_pala.iterrows():
        
        print("Processing " + str(i) + "/" + str(len(kaava_pala)))
        
        item_dict = {"kaavakartta_sis_maar":[], "kaavakartta":[], "maaraykset": [], "selostus": [], "oas": [], "muu": []}
        
        kaavatunnus = row['kaavatunnus']
        """
        try:
            if int(kaavatunnus) < 10:
                kaavatunnus = '0' + str(kaavatunnus)
        except ValueError:
            None
        """
        for idx, rivi in link_pala.iterrows():
            
            try:
                
                if int(kaavatunnus) == int(rivi['Kunnan indeksitunnus']):
                    
                    if int(rivi['Dokumentin tyyppi2']) == 1:
                        item_dict['kaavakartta_sis_maar'].append(rivi['Original filename'])
                    elif int(rivi['Dokumentin tyyppi2']) == 2:
                        item_dict['kaavakartta'].append(rivi['Original filename'])
                    elif int(rivi['Dokumentin tyyppi2']) == 3:
                        item_dict['maaraykset'].append(rivi['Original filename'])
                    elif int(rivi['Dokumentin tyyppi2']) == 4:
                        item_dict['selostus'].append(rivi['Original filename'])                
                    elif int(rivi['Dokumentin tyyppi2']) == 5:
                        item_dict['oas'].append(rivi['Original filename'])
                    elif int(rivi['Dokumentin tyyppi2']) == 6:
                        item_dict['muu'].append(rivi['Original filename'])
                    else:
                        None
                        
            except ValueError:
                
                if kaavatunnus == rivi['Kunnan indeksitunnus']:
                    
                    if int(rivi['Dokumentin tyyppi2']) == 1:
                        item_dict['kaavakartta_sis_maar'].append(rivi['Original filename'])
                    elif int(rivi['Dokumentin tyyppi2']) == 2:
                        item_dict['kaavakartta'].append(rivi['Original filename'])
                    elif int(rivi['Dokumentin tyyppi2']) == 3:
                        item_dict['maaraykset'].append(rivi['Original filename'])
                    elif int(rivi['Dokumentin tyyppi2']) == 4:
                        item_dict['selostus'].append(rivi['Original filename'])                
                    elif int(rivi['Dokumentin tyyppi2']) == 5:
                        item_dict['oas'].append(rivi['Original filename'])
                    elif int(rivi['Dokumentin tyyppi2']) == 6:
                        item_dict['muu'].append(rivi['Original filename'])
                    else:
                        None
            
        # Skenaario 1: kaavakartta (sis. määräykset)
        if len(item_dict['kaavakartta_sis_maar']) == 1:
            copy_kaavapala.at[index, 'kaavakartta'] = item_dict['kaavakartta_sis_maar'][0]
            copy_kaavapala.at[index, 'maaraykset'] = item_dict['kaavakartta_sis_maar'][0]
        elif len(item_dict['kaavakartta_sis_maar']) == 0:
            None
        else:
            sys.exit("Samalle kohteelle löytyi useampi kaavakartta, joissa on mukana myös määräykset!")
        
        # Skenaario 2: kaavakartta (ei määräyksiä)
        if len(item_dict['kaavakartta']) == 1:
            copy_kaavapala.at[index, 'kaavakartta'] = item_dict['kaavakartta'][0]
        elif len(item_dict['kaavakartta']) == 0:
            None
        else:
            sys.exit("Samalle kohteelle löytyi useampi kaavakartta, joissa ei ole mukana määräyksiä!")
        
        # Skenaario 3: määräykset (yliajaa skenaarion 1 määräykset tarvittaessa)
        if len(item_dict['maaraykset']) == 1:
            copy_kaavapala.at[index, 'maaraykset'] = item_dict['maaraykset'][0]
        elif len(item_dict['maaraykset']) == 0:
            None
        else:
            sys.exit("Samalle kohteelle löytyi useampi kaavamääräys!")
        
        # Skenaario 4: selostukset
        if len(item_dict['selostus']) == 1:
            copy_kaavapala.at[index, 'selostus'] = item_dict['selostus'][0]
        elif len(item_dict['selostus']) == 0:
            None
        else:
            sys.exit("Samalle kohteelle löytyi useampi kaavaselostus!")
    
        i = i + 1
        
    return(copy_kaavapala)
    
joined = joinPDFsToKaavadata(kaavadata=kaava_data,
                         link_table=data,
                         kuntakoodi="178",
                         kaavalaji="ak")
    
    #spatiaalihaku niille, joilla vain ktj-tunnus (tästä jo pohjat) --> uuden tunnuksen luominen
    #linkityskäsittely (joihin pohjat jo ylhäällä)
    
    #''.join([n for n in phone_number if n.isdigit()])

joined.to_file(r"G:\Oma Drive\Liiketoiminta\Suomen ympäristökeskus\VOOKA\Python\testi.gpkg", layer='testimme', driver="GPKG")
