from pprint import pprint
import requests
import json
from bs4 import BeautifulSoup


url = ('https://api.odcloud.kr/api/15086178/v1/uddi:c4193d9c-bb74-454a-980f-9421967e918b?serviceKey=DVNwYfz2bCeyEZsFkEwESH6ZvoZpDUhj%2FJ5em%2FruYkH7Fe%2FSmf48qyGZRbH2uKDbCP8M1NoY8SnBQzPJlQfdbA%3D%3D&page=1&perPage=50&returnType=json')
#남구 api의 URL에서 request 객체 생성
response = requests.get(url)

#데이터 값 출력
contents = response.text
#json으로 변경
json_ob = json.loads(contents)

#필요한 내용만 꺼내기
body = json_ob['data']
#pprint(body)