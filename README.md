# daegu-AirPump
### version
: python(3.8)

+ ### start.sh
1. 로컬서버(port=9999) 생성
2. flask 실행
+ ### app.py
1. Namgu.py 실행하고 Namgu import
2. Map.html 실행 body JSON을 value로 받음
+ ### Namgu.py
1. 남구 공기주입기api 받아오기
2. json으로 변경
3. 필요한 데이터만 꺼내기
+ ### Map.html
1. value를 array object에 저장
2. array의 length만큼 반복
3. 좌표 가져와서 마킹



+ ### ScrapeAirPump
1. ScrapeAirPump가 대구 자전거 공기주입기의 위치를 스크랩해준다
2. 공기주입기 주소를 addresses list에 저장
## 문제점
1. 데이터 질 쓰레기
