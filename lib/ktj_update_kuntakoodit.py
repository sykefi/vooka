# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 11:14:34 2022

@author: smassine
"""

def updateOldKuntakoodi(ktj_data):

    import geopandas as gpd

    ktj_data['validkuntanro'] = None
    
    # Tiputetaan pois Etelä-Savoon kuulumattomat rivit
    drop_list = ['077', '081', '090', '111', '163', '171', '172', '212', '248', '260', '286', '420', '580', '686', '700', '739', '778', '831', '850', '915']
    ktj_data = ktj_data[~ktj_data['kaavatunnuksenkuntanumero'].isin(drop_list)]
    
    for index, row in ktj_data.iterrows():
        
        #491
        if row['kaavatunnuksenkuntanumero'] == '085' or row['kaavatunnuksenkuntanumero'] == '492' or row['kaavatunnuksenkuntanumero'] == '696' or row['kaavatunnuksenkuntanumero'] == '775':
            ktj_data.at[index, 'validkuntanro'] ='491'
            
        #740
        elif row['kaavatunnuksenkuntanumero'] == '246' or row['kaavatunnuksenkuntanumero'] == '618' or row['kaavatunnuksenkuntanumero'] == '741':
            ktj_data.at[index, 'validkuntanro'] = '740'
       
        #593
        elif row['kaavatunnuksenkuntanumero'] == '184' or row['kaavatunnuksenkuntanumero'] == '594' or row['kaavatunnuksenkuntanumero'] == '640' or row['kaavatunnuksenkuntanumero'] == '937':
            ktj_data.at[index, 'validkuntanro'] = '593'
            
        else:
            ktj_data.at[index, 'validkuntanro'] = row['kaavatunnuksenkuntanumero']
            
    return(ktj_data)
