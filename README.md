# tourism

## traffic.py
- 전국 기차역 또는 버스터미널 위치정보 확인
```json
// 기차역
[
    {
        "city":11,
        "name":"서울역",
        "upperAddrName":"서울",
        "middleAddrName":"용산구",
        "lowerAddrName":"동자동",
        "detailBizName":"경부선",
        "latitude":"37.55320558",
        "longitude":"126.96927224"
    },
    {
        "city":11,
        "name":"용산역",
        "upperAddrName":"서울",
        "middleAddrName":"용산구",
        "lowerAddrName":"한강로3가",
        "detailBizName":"고속철도",
        "latitude":"37.53093031",
        "longitude":"126.96491216"
    },
    {
        "city":11,
        "name":"청량리역",
        "upperAddrName":"서울",
        "middleAddrName":"동대문구",
        "lowerAddrName":"전농동",
        "detailBizName":"중앙선",
        "latitude":"37.58112039",
        "longitude":"127.04665329"
    },
    {
        "city":11,
        "name":"수색역",
        "upperAddrName":"서울",
        "middleAddrName":"은평구",
        "lowerAddrName":"수색동",
        "detailBizName":"경의선",
        "latitude":"37.58217310",
        "longitude":"126.89494486"
    },
]

// 버스터미널
[
    {
        "city":11,
        "name":"서울역전시외버스터미널",
        "upperAddrName":"서울",
        "middleAddrName":"중구",
        "lowerAddrName":"봉래동2가",
        "detailBizName":"시외",
        "latitude":"37.55773287",
        "longitude":"126.97154968"
    },
    {
        "city":11,
        "name":"서울고속버스터미널 경부영동선",
        "upperAddrName":"서울",
        "middleAddrName":"서초구",
        "lowerAddrName":"반포동",
        "detailBizName":"고속",
        "latitude":"37.50579505",
        "longitude":"127.00454814"
    },
    {
        "city":11,
        "name":"신세계센트럴시티터미널 호남선",
        "upperAddrName":"서울",
        "middleAddrName":"서초구",
        "lowerAddrName":"반포동",
        "detailBizName":"고속",
        "latitude":"37.50348976",
        "longitude":"127.00454821"
    },
    {
        "city":11,
        "name":"서울남부터미널",
        "upperAddrName":"서울",
        "middleAddrName":"서초구",
        "lowerAddrName":"서초동",
        "detailBizName":"종합",
        "latitude":"37.48474215",
        "longitude":"127.01613102"
    },
]

```
- 참고
  - [SK Open API](https://openapi.sk.com/)
  - [T map API docs](http://tmapapi.sktelecom.com/main.html#webservice/docs/tmapRouteDoc)

## keyword.py
- 연관어 unique 적용하기 
```json
[
   '우수성을',
   '분위기의',
   '최대',
   '라운지가',
   '가성비짱',
   '뒤를',
   '우리집은',
   '서울대',
   '한참을',
   '요즘유행하는코디',
 ]
```
