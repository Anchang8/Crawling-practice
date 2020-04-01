from bs4 import BeautifulSoup
from pprint import pprint
import requests, re, os
from urllib.request import urlretrieve
from urllib.parse import quote_plus

a=input('검색어를 입력하세요.')
try:
    if not (os.path.isdir(a)):
        os.makedirs(os.path.join(a))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 생성 실패!")
        exit()
#웹 페이지를 열고 소스코드를 읽어오는 작업
html = requests.get("https://search.naver.com/search.naver?where=image&sm=tab_jum&query="+quote_plus(a))
soup = BeautifulSoup(html.text, 'html.parser')
html.close()

#요일별 웹툰영역 추출하기
data1_list=soup.find('div',{'class':'photo_grid _box'})

data2=data1_list.findAll('div',{'class':'img_area _item'})
for x in range(len(data2)):
    img=data2[x].find('img')
    img_src=img['data-source']
    urlretrieve(img_src, './'+a+'/'+str(x)+'.jpg')
print('다운로드 완료')        
