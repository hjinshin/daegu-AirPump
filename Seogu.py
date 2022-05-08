from pprint import pprint
import re
import requests
import json
from bs4 import BeautifulSoup


req = requests.get('https://www.dgs.go.kr/dgs/life/page.php?mnu_uid=11346&')
req.encoding='utf-8'
soup=BeautifulSoup(req.text, 'html.parser')

addresses = []

#div class="tabl" 추출
divs = soup.findAll('div',{"class": "tabl"})
for div in divs:

    boxes = div.findAll('tr')
    for box in boxes:
        #td style="border-width: 0px 0.5pt 0.5pt 0px; border-style: none solid solid none; border-color: black windowtext windowtext black; background-color: transparent;" 추출
        temps = box.findAll('td', {"style": "border-width: 0px 0.5pt 0.5pt 0px; border-style: none solid solid none; border-color: black windowtext windowtext black; background-color: transparent;"})

        #표 1칸씩 infos 리스트에 저장
        infos = []
        for temp in temps:
            lines = temp.findAll('span', {"style": "font-family: 맑은 고딕; font-size: 10pt;"})

            #필요한 정보는 lines[0]
            for line in lines:

                if lines.index(line) % 2 == 0:
                    ads = line
                    for ad in ads:
                        info = ad.text

                        info = info.replace('\r', '')
                        info = info.replace('\n', '')
                        info = info.replace('  ', '')

                        # 괄호 제거
                        rmve_bracket = "\(.*\)|\s-\s.*"
                        info = re.sub(rmve_bracket, '', info)
                        info = info.replace('(', '')

                        info = "대구광역시 " + info
                        infos.append(info)

        if(len(infos)>=4):
            addresses.append(infos[1])


address_json = []
for cnt in addresses:
    dic = {}
    dic['도로명'] = cnt
    address_json.append(dic)


body = json.dumps(address_json, ensure_ascii=False)


#pprint(body)
with open('AirPump.txt','w',encoding='UTF-8') as f:
    for i in addresses:
        f.write( i +'\n')



