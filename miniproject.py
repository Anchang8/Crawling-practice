'''
pip install request beautifulsoup4
'''
import requests     #웹 소스를 열어서 읽을수 있게해줌
from bs4 import BeautifulSoup
import time
import json
access_token="rL2RE0AiEciP6Whmu3QN1JUS6jwAJjhMk3jn5wo9cpcAAAFxPkWA3g"
def send_to_kakao(text):
    header = {"Authorization": 'Bearer ' + access_token}
    url="https://kapi.kakao.com/v2/api/talk/memo/default/send"
    post={
        "object_type": "text",
        "text": text,
        "link": {
            "web_url": "https://developers.kakao.com",
            "mobile_web_url": "https://developers.kakao.com"
        },
    }
    data={"template_object": json.dumps(post)}
    return requests.post(url, headers=header,data=data)
    
def search():
    url2="https://www.edaily.co.kr/article/society"
    r=requests.get(url2)
    bs=BeautifulSoup(r.content,'lxml')
    divs=bs.select("ul.newsbox_texts") #select의 결과는 list이다
    for x in divs:
        if "서울" in str(x) and "코로나" in str(x): #"경산" in str(x) and "코로나" in str(x) and "확진" in str(x):
            a=[]
            a.append(str(x))
            if count==0:
                b.append(str(x))
            
            if count==0:
                for z in a:
                    send_to_kakao(str(z))
            if count>0:
                for u in a:
                    if u not in b:
                        send_to_kakao(str(u))
            
            if str(x) not in b:
                b.append(str(x))
            
    
 
if __name__== "__main__":
    global count
    count=0
    a=[]
    b=[]
    while True:
        print(count)
        search()
        count+=1
        time.sleep(60)#1시간에 한번씩 검사해서 알려
