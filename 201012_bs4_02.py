# -*- coding: utf-8 -*-

## 1. url 링크 확보
## 2. url에서 html 정보 가져옴
## 3. 얻어온 정보를 bs4로 구조화
## 4. soup.find, soup.find_all 등을 이용해 정보 가져옴

from urllib.request import urlopen
from bs4 import BeautifulSoup

url="https://finance.naver.com/sise"

page=urlopen(url)

soup=BeautifulSoup(page, 'html.parser')

#%% 정보 가져오기
# 네이버 코스피, 코스닥, 코스피200

kospi=soup.find("span", id='KOSPI_now')
print('현재 코스피 :', kospi.text)

#%% 실습 3-2 코스닥, 코스피200 지수 가져오기

kosdaq=soup.find("span", id='KOSDAQ_now')
print('현재 코스닥 :', kosdaq.text)

kpi200=soup.find("span", id='KPI200_now')
print('현재 코스피200 :', kpi200.text)

#%% 심화 3-2 : 인기 10종목 가져오기
top10=soup.find("ul", class_='lst_pop', id="popularItemList")
print(top10.text)

#%% 심화 3-2 두번째 방법
li_all=soup.find("ul", class_='lst_pop')

a_all=li_all.find_all('a')
li_span=li_all.find_all("span")

for i in a_all:
    print(i.text)

cnt=0
for i in li_span:
    if cnt%2==0:
        print(i.text)
    cnt=cnt+1
