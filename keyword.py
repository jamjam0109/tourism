# !pip install xlrd
import pandas as pd
import numpy as np
import os

def get_site_name(file_name):
    return file_name.split(' ')[1].split('_')[0]


'''
path: data가 저장되어 있는 경로
'''

def r(path):
    # 폴더 내 파일 명 가져오기 
    file_names = os.listdir(path)

    output = list()
    # site_names = list()

    for file_name in file_names:

        df = pd.read_excel(f'{path}/{file_name}')

        # 관광지 명 가져오기 
        site_name = get_site_name(file_name)
        # site_names.append(site_name)
  
        # 연관어 가져오기 
        keyword = df['연관어'].tolist()
        print(f'{file_name}: {len(keyword)}')
        # 연관어에서 관광지 명 삭제
        keyword.remove(site_name)

        # extend 
        output.extend(keyword)
    
    # unique
    unique_output = list(set(output))
    
    return unique_output

path = './data'
output = r(path)