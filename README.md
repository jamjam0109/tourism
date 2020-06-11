# tourism

## traffic.py
- 전국 기차역 또는 버스터미널 위치정보 확인

- 결과 예제
```json
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
    {
        "city":26,
        "name":"부산역",
        "upperAddrName":"부산",
        "middleAddrName":"동구",
        "lowerAddrName":"초량동",
        "detailBizName":"경부선",
        "latitude":"35.11432711",
        "longitude":"129.04090562"
    },
    {
        "city":26,
        "name":"구포역",
        "upperAddrName":"부산",
        "middleAddrName":"북구",
        "lowerAddrName":"구포동",
        "detailBizName":"경부선",
        "latitude":"35.20570496",
        "longitude":"128.99749024"
    },
    {
        "city":26,
        "name":"부산진역",
        "upperAddrName":"부산",
        "middleAddrName":"동구",
        "lowerAddrName":"수정동",
        "detailBizName":"경부선",
        "latitude":"35.12907561",
        "longitude":"129.04937670"
    },
    {
        "city":26,
        "name":"부전역",
        "upperAddrName":"부산",
        "middleAddrName":"부산진구",
        "lowerAddrName":"부전동",
        "detailBizName":"동해선",
        "latitude":"35.16362750",
        "longitude":"129.06062478"
    },
    {
        "city":26,
        "name":"사상역",
        "upperAddrName":"부산",
        "middleAddrName":"사상구",
        "lowerAddrName":"괘법동",
        "detailBizName":"경부선",
        "latitude":"35.16254296",
        "longitude":"128.98843665"
    },
]
```

- 참고
  - [SK Open API](https://openapi.sk.com/)
  - [T map API docs](http://tmapapi.sktelecom.com/main.html#webservice/docs/tmapRouteDoc)
