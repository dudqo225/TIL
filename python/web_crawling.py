### 지니TOP200 중 1위 곡/가수 불러오기 ###

# Web Crawling 에 필요한 라이브러리 Import
import requests
from bs4 import BeautifulSoup

# 지니 URL 변수 저장
url = 'https://www.genie.co.kr/chart/top200'

# requests 라이브러리를 활용하여 data 추출
response = requests.get(url, headers={'User-agent' : 'Mozilla/5.0'}) # headers 설정 이유 : 기계가 아닌 사람이 접속했다는 것을 보여주기 위해서
data = BeautifulSoup(response.text, 'html.parser')

# 노래/가수 제목 추출 - CSS Selector
song = data.select_one('#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis')
singer = data.select_one('#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis')

# f 포맷팅으로 원하는 방식으로 표현
text = f'현재 지니 1위는 {singer.text.strip()}의 {song.text.strip()} 입니다.'

print(text)