import requests
from bs4 import BeautifulSoup

#주소를 저장할 리스트
detail_addresses = []
addresses = []

#대구 홈페이지에서 request 객체 생성
req = requests.get('https://www.daegu.go.kr/tra/index.do?menu_id=00934290')
soup = BeautifulSoup(req.text, 'html.parser')

#div class="conBox" 추출
divs = soup.findAll('div', {"class": "conBox"})
for div in divs:
    #<tr> 태그 추출
    links = div.findAll('tr')

    #td class="tal" 추출
    for link in links:
        ads = div.findAll('td', {"class":"tal"})

        for ad in ads:
            # td class="tal" 태그 내부의 텍스트를 리스트에 삽입
            address = ad.text
            #상세 주소 저장
            detail_addresses.append(address)

            #마지막에 '.' 입력
            address = address + '.'

            #검색어 변환
            address = address.replace('출입구', '출구') #출입구->출구
            #address = address.replace("(","").replace(")","") #괄호 제거

            addresses.append(address)

with open('AirPump.txt','w',encoding='UTF-8') as f:
    for name in addresses:
        f.write(name+'\n')