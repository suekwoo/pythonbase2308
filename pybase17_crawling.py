# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 14:39:35 2023

@author: KITCOOP
"""

# 빅데이터 종류
# 1. 정형데이터 : csv, excel, db table
# 2. 반정형데이터 : html, xml, json ...
#                  크롤링.
#                  BeautifulSoup, Selenium 모듈
# 3. 비정형데이터 : 이미지,동영상,...

from bs4 import BeautifulSoup #html,xml 파싱 모듈
import urllib.request as req
url="https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
res=req.urlopen(url)
soup = BeautifulSoup(res,"html.parser")
title=soup.find("title").string #title 태그 선택
title
wf=soup.find("wf").string  #wf 태그 선택
title
wf


# wf 데이터를 <br /> 문자열로 분리하여 화면에 출력하기
for w in wf.split("<br />") :
    print(w)

#인터넷에서 수신된 내용을 forecast.xml 파일로 저장하기
import os.path
# os.path.exists : 파일 존재?
if not os.path.exists("data/forecast.xml") :
#urlretrieve : 인터넷을 통해 전달받은 데이터를 파일로 저장    
#urlretrieve(url, 저장할 파일명)
    req.urlretrieve(url,"data/forecast.xml")

#forecast.xml 파일을 읽어서 BeautifulSoup 객체로 분석하기
fp = open("data/forecast.xml",encoding="utf-8")
soup = BeautifulSoup(fp,"html.parser")
#select_one : 태그한개 선택.
#rss pubDate : rss 태그의 하위 태그 중 pubDate 태그 선택
pubdate = soup.select_one("rss pubDate").string
pubdate




#select : 태그 여러개를 리스트로 리턴.
rss = soup.select("rss")[0] #rss 태그들중 첫번째.
rss
#첫번째 rss태그의 하위 태그 중 pubDate 태그의 내용
pubdate = rss.select_one("pubDate").string
pubdate

#location 태그들의 하위 태그 중 한개의 city, wf 태그의 
# 내용 출력하기
for location in soup.select("location") :
    #location : location 태그 한개
   city = location.select_one("city").string                               
   wf = location.select_one("wf").string
   tmn = location.select_one("tmn").string
   tmx = location.select_one("tmx").string
   print(city,wf,tmn,tmx)


#find_all : location 태그 들
#find : city 태그 한개
for location in soup.find_all("location") :
    #location : location 태그 한개
   city = location.find("city").string                               
   wf = location.find("wf").string
   tmn = location.find("tmn").string
   tmx = location.find("tmx").string
   print(city,wf,tmn,tmx)


#네이버 환율정보 조회하기
url= "https://finance.naver.com/marketindex/"
res = req.urlopen(url)
soup = BeautifulSoup(res,"html.parser") #DOM tree
#sel 함수 정의 : 람다방식
sel = lambda q : soup.select(q)
#div.head_info : div 태그 중 class 속성이 head_info 태그들
hlist = sel("div.head_info") #환율정보 태그들
print(hlist)
htitle = sel("h3.h_lst") #통화명 태그들
print(htitle)

#그래프 출력을 위해 데이터 저장
taglist=[] #상승/하락 값
titlelist=[] #통화명
for tag, title in zip(hlist, htitle) :
    #tag : 환율정보, title:통화명.
    print(title.select_one("span.blind").string, end="\t")
    value = tag.select_one("span.value").string #환율정보
    print(value, end=" ")
    change = tag.select_one("span.change").string #상승/하락값
    print(change, end="\t")
    blinds = tag.select("span.blind") #통화단위
    b = tag.select("span.blind")[0].string #첫번째 통화단위
    b = tag.select("span.blind")[-1].string #상승,하락
    print(b, end="*******\n")    
    if b == '하락' :
       taglist.append(float(change) * -1) #하락인 경우 음수
    else :
       taglist.append(float(change))
    #통화국가명 titlelist에 추가
    titlelist.append(title.select_one("span.blind").string)

print(taglist) 
print(titlelist)


#국내금데이터 제외.
titlelist = titlelist[:-1] #마지막데이터 제거
taglist = taglist[:-1]
print(taglist) 
print(titlelist)

#상승/하락 여부 그래프로 출력하기
import matplotlib.pyplot as plt
from matplotlib import  rc
plt.style.use("ggplot")
plt.rcParams['axes.unicode_minus']=False #음수표시
rc('font', family='Malgun Gothic')  #한글폰트
xlab = range(len(titlelist))
plt.bar(xlab,taglist) #막대그래프
plt.plot(xlab,taglist) #선그래프
#x축 설정. xlab x축의값을 titlelist의 값으로 변경.
#rotation='vertical' :세로표시
plt.xticks(xlab,titlelist,rotation='vertical')


###########################
# 셀레니움 모듈 : 브라우저를 직접 제어함 : 로그인, 버튼 클릭등

'''
  1. 크롬 브라우저의 버전 확인하기
     도움말 > 크롬정보 116.0.5845.141(공식 빌드) (64비트)
  2. http://chromedriver.chromium.org/downloads
    => 크롬 드라이버 다운받기. chromedriver_win32.zip
    chromedriver.exe 
  3. 압축풀기
  4. chromedriver.exe의 위치 정하기 : {workspace}/chrome
  5. anaconda prompt 에서 pip install selenium  
  driver = webdriver.Chrome(chromedriver.exe)  
  !!!!! 위의 내용은 하지 않는다
  driver = webdriver.Chrome()
'''
from selenium import webdriver #pip install selenium
import time
#chromedriver.exe : 크롬을 제어할수 있는 실행 파일
# 크롬에서 제공.
#브라우저 실행
driver = webdriver.Chrome()
# 브라우저에 "http://python.org" url 요청
driver.get("http://python.org")
time.sleep(1) #1초 대기







#find_elements : 선택된 태그 들
# css selector : css 언어에서 사용하는 선택자 방식
# #top ul.menu li : id="top" 인 태그의 하위 태그 중 
#                  class="menu"인 ul 태그. ul 태그의 하위
#                  li 태그들
menus = driver.find_elements("css selector",'#top ul.menu li')
menus[0].text
menus[1].text
for m in menus :
    #m : li 태그
    if m.text=="PyPI" :
        pypi = m #menu 중 PyPI인 값을 가진 메뉴
        print(m.tag_name,m.text)

pypi.click()  #li 객체를 클릭
time.sleep(5)
driver.quit()        

#브라우저 실행
### 네이버에 로그인 하기
'''
execute_script() : 자바스크립트 함수 실행.
       document.getElementsByName('id')[0].value='aaa'
       document.getElementsByName("id") : name 속성이 id인 태그 들
find_elements(선택방법,선택자) : 여러개 태그 선택 => selenium 4버전이후
find_element(선택방법,선택자) : 하나의 태그 선택
       xpath : xml방식으로 태그 찾아가는 방법
             //*[@id="log.login"] : id속성값이 log.login 인 태그 한개 선택.
                 // : root 노드. 최상위 노드. 처음부터
                 *  : 모든태그
                 [] : 속성값
                 @id : id속성
                 log.login : id속성 값
                 
  선택방법에 사용되는 문자열
   By.XPATH        : "xpath" : xml에서 사용되는 태그 검색 방식
   By.CLASS_NAME   : "class name" : class 속성값
   By.CSS_SELECTOR : "css selector" : css 문서에서 사용하는 선택자 방식      
   By.ID           : "id"    : id 속성값
   By.TAG_NAME     : "tag name" : 태그이름      
'''





driver = webdriver.Chrome()

driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")
#input : 화면에서 문자열 입력
id = input("네이버 아이디를 입력하세요:")
#아이디 칸에 입력된 네이버아이디 전달
driver.execute_script("document.getElementsByName('id')[0].value='"+id+"'")
pw = input("네이버 비밀번호를 입력하세요 : ")
time.sleep(1)
driver.execute_script\
("document.getElementsByName('pw')[0].value='"+pw+"'")
time.sleep(1)
driver.find_element('xpath','//*[@id="log.login"]').click()





# daum 페이지에서 이미지 다운받아 저장하기
driver = webdriver.Chrome()
driver.get("https://search.daum.net/search?w=img&nil_search=btn&DA=NTB&enc=utf8&q=%EC%9E%A5%EB%AF%B8" )
time.sleep(3)
#images : 다음페이지의 img 태그목록들 
images = driver.find_elements("css selector","div.wrap_thumb > a.thumb_bf > img")
images[0]
len(images)
img_url = []
for image in images :
    #image : <img src='....'>태그 한개
    url = image.get_attribute('src') #src 속성값
    img_url.append(url) #이미지 저장 url 
print(img_url[0])


import time
import urllib.request as req 
import os 
#img_url의 목록을 다운받아 img 폴더에 저장
img_folder = './img' #현재 폴더 하위의 img 폴더
if not os.path.isdir(img_folder) :  #폴더 아님?
    os.mkdir(img_folder)    #폴더 생성
for index, link in enumerate(img_url) :
    #index : 리스트의 순서
    #link : url 정보
    #urlretrieve : url의 결과를 파일로 저장
	req.urlretrieve(link, f'./img/{index}.jpg')















