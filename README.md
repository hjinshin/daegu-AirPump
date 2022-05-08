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
+ ### Seogu.py
1. Seogu가 서구 자전거 공기주입기의 위치를 스크랩해준다
2. 필요한 정보만 추출
3. json으로 변경
+ ### Map.html
5. value를 array object에 저장
6. array의 length만큼 반복
7. 좌표 가져와서 마킹



## 문제점
1. 데이터 질 쓰레기
