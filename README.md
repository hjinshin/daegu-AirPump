# daegu-AirPump
### version
: python(3.8)

+ ### start.sh
1. 로컬서버(port=9999) 생성
2. flask 실행
+ ### app.py
1. ScrapeAirPump.py 실행하고 addresses list import
2. Map.html 실행 address list를 value로 받음
+ ### ScrapeAirPump.py
1. ScrapeAirPump가 대구 자전거 공기주입기의 위치를 스크랩해준다
2. 공기주입기 주소를 통째로 addresses list에 저장
+ ### Map.html
1. value list를 JSON으로 변경
2. value 길이만큼 검색 반복

## 문제점
1. 효율 최악(10000개 돌리면 9개 나옴)
   - 해결방안(예상?)
      1. (value Object를 띄어쓰기로 뒤에서부터 자름)
