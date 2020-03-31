from bs4 import BeautifulSoup
from pprint import pprint
import requests

#웹 페이지를 열고 소스코드를 읽어오는 작업
html = requests.get("http://comic.naver.com/webtoon/weekday.nhn")
soup = BeautifulSoup(html.text, 'html.parser')
html.close()
alllist=[]
data1=soup.findAll('div',{'class':'col_inner'})
for x in range(len(data1)):
    data2=data1[x].findAll('a',{'class':'title'})
    lista=[i.text for i in data2]
    alllist.append(lista)
a=input('순위를 찾고자 하는 웹툰이 무슨요일입니까? : ')
b=-1
while True:
    if a=='월요일':
        b=0
    elif a=='화요일':
        b=1
    elif a=='수요일':
        b=2
    elif a=='목요일':
        b=3
    elif a=='금요일':
        b=4
    elif a=='토요일':
        b=5
    elif a=='일요일':
        b=6
    else:
        a=input('다시 입력하시오 : ')
    if b>=0:
        break
c=input('순위를 찾고자 하는 웹툰의 이름을 정확히 입력하시오 : ')
l=alllist[b]
print(l.index(c)+1,'위 입니다')
