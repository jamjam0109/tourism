import requests
import json

def r(appKey, searchKeyword, areaLLCode):
    
    output = list()

    for area_code in areaLLCode:
        url = f'https://apis.openapi.sk.com/tmap/pois?appKey={appKey}&searchKeyword={searchKeyword}&radius=0&areaLLCode={area_code}'
        q = requests.get(url)
        json_output = json.loads(q.text)
        
        pois = json_output['searchPoiInfo']['pois']['poi']
        
        if searchKeyword == '버스터미널':

            exception = ['주차장', '정문', '영업소', '교통', '정류소', '여객', '운수', '정류장', '관광', '산업', '동관', '서관', '매표소', '속리산']

            for poi in pois:
                if poi['lowerBizName'] == '버스터미널' and '터미널' in poi['name'] and any(x in poi['detailBizName'] for x in ['고속', '종합', '시외']):
                    if any(x in poi['name'] for x in exception): 
                        continue
                    else:
                        x = {
                            'city': area_code,
                            'name': poi['name'],
                            'upperAddrName': poi['upperAddrName'],
                            'middleAddrName': poi['middleAddrName'],
                            'lowerAddrName': poi['lowerAddrName'],
                            'detailBizName': poi['detailBizName'],                            
                            'latitude': poi['frontLat'],
                            'longitude': poi['frontLon']
                        }

                        output.append(x)
                        
        elif searchKeyword == '기차역':

            exception = ['주차장', '입구', '취급소', '유실물', '정문', '예정', '폐역', '사무소', '진입로', '후문', '방면', '선로']
            
            for poi in pois:
                if poi['lowerBizName'] == '기차역' and '기타' not in poi['detailBizName']:
                    if any(x in poi['name'] for x in exception): 
                        continue
                    else:
                        x = {
                            'city': area_code,
                            'name': poi['name'],
                            'upperAddrName': poi['upperAddrName'],
                            'middleAddrName': poi['middleAddrName'],
                            'lowerAddrName': poi['lowerAddrName'],
                            'detailBizName': poi['detailBizName'],
                            'latitude': poi['frontLat'],
                            'longitude': poi['frontLon']
                        }

                        output.append(x)
    
    return output 

appKey = 'my_app_key' 
searchKeyword = '기차역' # 버스터미널 or 기차역
areaLLCode = [11, 26, 27, 28, 29, 30, 31, 36, 41, 42, 43, 44, 45, 46, 47, 48, 50] # 17개 시도 코드

output = r(appKey, searchKeyword, areaLLCode)