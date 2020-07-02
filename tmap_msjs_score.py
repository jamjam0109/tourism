import pandas as pd 

'''
index를 column으로 바꿔주는 함수

df: index가 존재하는 데이터프레임
'''
def convert_index_to_column(df):
    df.reset_index(level=0, inplace=True)

    return df


'''
tmap 맛집데이터를 기반으로 미식지수(msjs)를 산출하는 함수


input_path: tmap 맛집데이터 경로
output_path: 결과를 저장할 경로
'''
def tmap_msjs_score(input_path, output_path):

    df = pd.read_excel(input_path)

    groupby_address = df.groupby(['address_1', 'address_2']).count()['poi_id']
    groupby_address_df = pd.DataFrame(groupby_address)

    groupby_address_df = convert_index_to_column(groupby_address_df)
    groupby_address_df = convert_index_to_column(groupby_address_df)

    groupby_search = df.groupby(['address_1', 'address_2']).sum()['count']
    groupby_search_df = pd.DataFrame(groupby_search)

    groupby_search_df = convert_index_to_column(groupby_search_df)
    groupby_search_df = convert_index_to_column(groupby_search_df)

    merge_df = pd.merge(groupby_address_df, groupby_search_df, on=['address_1', 'address_2'])
    merge_df = merge_df[['address_1', 'address_2', 'poi_id', 'count']]
    merge_df.rename(columns = {'poi_id' : 'matjib_count', 'count': 'search_count'}, inplace = True)

    merge_df['score'] = merge_df['search_count'] / merge_df['matjib_count']

    merge_df.to_csv(output_path, index=False, encoding='utf-8-sig')


input_path = '../../data/tmap/tmap_mat.xlsx'
output_path = '../../output/tmap_mat_output.csv'

tmap_msjs_score(input_path, output_path)