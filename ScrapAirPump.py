import requests
from bs4 import BeautifulSoup

addresses = []

req = requests.get('https://www.daegu.go.kr/tra/index.do?menu_id=00934290')
soup = BeautifulSoup(req.text, 'html.parser')

divs = soup.findAll('div', {"class": "conBox"})
for div in divs:
    links = div.findAll('tr')

    for link in links:
        ads = div.findAll('td', {"class":"tal"})

        for ad in ads:
            address = ad.text
            addresses.append(address)

with open('AirPump.txt','w',encoding='UTF-8') as f:
    for name in addresses:
        f.write(name+'\n')